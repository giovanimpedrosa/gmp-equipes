from django.db import models
from projects.models import Project

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]
    
    STATUS_CHOICES = [
        ('todo', 'A Fazer'),
        ('doing', 'Em Andamento'),
        ('done', 'Concluída'),
    ]

    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    due_date = models.DateTimeField('Data de entrega')
    priority = models.CharField(
        'Prioridade',
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    status = models.CharField(
        'Status',
        max_length=5,
        choices=STATUS_CHOICES,
        default='todo'
    )
    project = models.ForeignKey(
        Project,
        verbose_name='Projeto',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'tasks_task'
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['due_date']

    def __str__(self):
        return self.title

    def get_priority_color(self):
        return {
            'low': 'success',
            'medium': 'warning',
            'high': 'danger'
        }.get(self.priority, 'secondary')

    def get_status_color(self):
        return {
            'todo': 'secondary',
            'doing': 'primary',
            'done': 'success'
        }.get(self.status, 'secondary')