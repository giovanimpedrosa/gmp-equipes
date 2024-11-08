from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from projects.models import Project

@login_required
def task_list(request):
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', 'due_date')
    direction = request.GET.get('direction', 'asc')
    view_type = request.GET.get('view', 'grid')
    
    tasks = Task.objects.filter(project__owner=request.user)
    
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(project__title__icontains=search)
        )
    
    order_by = f"{'-' if direction == 'desc' else ''}{sort}"
    tasks = tasks.order_by(order_by)
    
    columns = [
        {'key': 'title', 'label': 'Título', 'sortable': True},
        {'key': 'project', 'label': 'Projeto', 'sortable': True},
        {'key': 'due_date', 'label': 'Prazo', 'sortable': True},
        {'key': 'priority', 'label': 'Prioridade', 'sortable': True},
        {'key': 'status', 'label': 'Status', 'sortable': True},
    ]
    
    paginator = Paginator(tasks, 10)
    page = request.GET.get('page', 1)
    tasks = paginator.get_page(page)
    
    context = {
        'items': tasks,
        'columns': columns,
        'view_name': 'tasks',
        'view_type': view_type
    }
    
    if request.headers.get('HX-Request'):
        return render(request, 'components/datatable_content.html', context)
    return render(request, 'tasks/task_list.html', context)

@login_required
def task_create(request):
    initial_project = request.GET.get('project')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Verifica se o usuário é dono do projeto
            if task.project.owner != request.user:
                messages.error(request, 'Você não tem permissão para criar tarefas neste projeto.')
                return redirect('projects:list')
            task.save()
            return redirect('tasks:detail', pk=task.pk)
    else:
        initial = {}
        if initial_project:
            project = get_object_or_404(Project, pk=initial_project, owner=request.user)
            initial['project'] = project
        form = TaskForm(initial=initial)
        # Filtrar projetos do usuário no form
        form.fields['project'].queryset = Project.objects.filter(owner=request.user)
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'action': 'Criar'
    })

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if task.project.owner != request.user:
                messages.error(request, 'Você não tem permissão para editar esta tarefa.')
                return redirect('projects:list')
            task.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('tasks:detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
        form.fields['project'].queryset = Project.objects.filter(owner=request.user)
    
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'task': task,
        'action': 'Editar'
    })

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    if request.method in ['DELETE', 'POST']:  # Suporta tanto DELETE quanto POST
        task.delete()
        if request.headers.get('HX-Request'):  # Se for requisição HTMX
            return HttpResponse('')  # Retorna vazio para remover o elemento
        return redirect('tasks:list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_change_status(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            task.save()
            
            # Retorna apenas o elemento atualizado
            return render(request, 'tasks/partials/task_status.html', {'task': task})
    return HttpResponse(status=400)

@login_required
def task_list_partial(request):
    project_id = request.GET.get('project')
    if project_id:
        tasks = Task.objects.filter(project__owner=request.user, project_id=project_id)
    else:
        tasks = Task.objects.filter(project__owner=request.user)
    return render(request, 'tasks/partials/task_list.html', {'tasks': tasks}) 