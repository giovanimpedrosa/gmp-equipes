from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from projects.models import Project
from tasks.models import Task

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    # Obtém os projetos do usuário
    projects = Project.objects.filter(owner=request.user)
    
    # Obtém as tarefas dos projetos do usuário
    tasks = Task.objects.filter(project__owner=request.user)
    
    # Estatísticas
    stats = {
        'total_projects': projects.count(),
        'total_tasks': tasks.count(),
        'tasks_todo': tasks.filter(status='todo').count(),
        'tasks_doing': tasks.filter(status='doing').count(),
        'tasks_done': tasks.filter(status='done').count(),
        'tasks_by_priority': {
            'high': tasks.filter(priority='high').count(),
            'medium': tasks.filter(priority='medium').count(),
            'low': tasks.filter(priority='low').count(),
        }
    }
    
    # Tarefas próximas do prazo (próximos 7 dias)
    from django.utils import timezone
    from datetime import timedelta
    upcoming_tasks = tasks.filter(
        due_date__range=[
            timezone.now(),
            timezone.now() + timedelta(days=7)
        ]
    ).order_by('due_date')[:5]
    
    # Projetos recentes
    recent_projects = projects.order_by('-created_at')[:3]
    
    context = {
        'stats': stats,
        'upcoming_tasks': upcoming_tasks,
        'recent_projects': recent_projects,
    }
    
    return render(request, 'users/dashboard.html', context)

@login_required
def update_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        if theme in ['light', 'dark']:
            request.user.theme_preference = theme
            request.user.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)