from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import HttpResponse
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

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('projects:detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form, 'action': 'Criar'})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {
        'form': form,
        'project': project,
        'action': 'Editar'
    })

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method in ['DELETE', 'POST']:
        project.delete()
        if request.headers.get('HX-Request'):
            return HttpResponse('')
        return redirect('projects:list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project}) 