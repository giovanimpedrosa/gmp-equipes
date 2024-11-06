from django.db import models
from django.conf import settings

class Project(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Proprietário',
        on_delete=models.CASCADE,
        related_name='projects'
    )

    class Meta:
        db_table = 'projects_project'
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title 