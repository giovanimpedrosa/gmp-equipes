from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm

@login_required
def project_list(request):
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', '-created_at')
    direction = request.GET.get('direction', 'asc')
    view_type = request.GET.get('view', 'grid')
    
    projects = Project.objects.filter(owner=request.user).annotate(
        tasks_count=Count('tasks')
    )
    
    if search:
        projects = projects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )
    
    order_by = f"{'-' if direction == 'desc' else ''}{sort}"
    projects = projects.order_by(order_by)
    
    columns = [
        {'key': 'title', 'label': 'Título', 'sortable': True},
        {'key': 'description', 'label': 'Descrição', 'sortable': False},
        {'key': 'value', 'label': 'Valor', 'sortable': True, 'type': 'decimal'},
        {'key': 'is_active', 'label': 'Ativo', 'sortable': True, 'type': 'boolean'},
        {'key': 'created_at', 'label': 'Criado em', 'sortable': True},
    ]
    
    paginator = Paginator(projects, 10)
    page = request.GET.get('page', 1)
    projects = paginator.get_page(page)
    
    context = {
        'items': projects,
        'columns': columns,
        'view_name': 'projects',
        'view_type': view_type
    }
    
    if request.headers.get('HX-Request'):
        return render(request, 'components/datatable_content.html', context)
    return render(request, 'projects/project_list.html', context)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Criar'
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Atualizar'
        return context

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method in ['DELETE', 'POST']:
        project.delete()
        if request.headers.get('HX-Request'):
            return HttpResponse('')
        return redirect('projects:list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project}) 