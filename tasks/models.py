from django.db import models
from django.conf import settings
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
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['due_date']

    def __str__(self):
        return self.title

    def get_priority_display_class(self):
        return {
            'low': 'bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200',
            'medium': 'bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200',
            'high': 'bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200'
        }.get(self.priority, '')

    def get_status_display_class(self):
        return {
            'todo': 'bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200',
            'doing': 'bg-blue-100 dark:bg-blue-700 text-blue-800 dark:text-blue-200',
            'done': 'bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200'
        }.get(self.status, '')