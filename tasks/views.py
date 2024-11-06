from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm
from projects.models import Project

@login_required
def task_list(request):
    project_id = request.GET.get('project')
    if project_id:
        tasks = Task.objects.filter(project__owner=request.user, project_id=project_id)
    else:
        tasks = Task.objects.filter(project__owner=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    project_id = request.GET.get('project')
    initial = {'project': project_id} if project_id else None
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # Verificar se o usuário é dono do projeto
            if task.project.owner != request.user:
                messages.error(request, 'Você não tem permissão para criar tarefas neste projeto.')
                return redirect('projects:list')
            task.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('tasks:detail', pk=task.pk)
    else:
        form = TaskForm(initial=initial)
        # Filtrar projetos do usuário no form
        form.fields['project'].queryset = Project.objects.filter(owner=request.user)
    
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Criar'})

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
    if request.method == 'POST':
        project_id = task.project.id
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('projects:detail', pk=project_id)
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def task_change_status(request, pk):
    if request.method == 'POST' and request.is_ajax():
        task = get_object_or_404(Task, pk=pk, project__owner=request.user)
        new_status = request.POST.get('status')
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            task.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400) 