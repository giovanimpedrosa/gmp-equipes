from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    detailed_description = RichTextField('Descrição Detalhada', null=True, blank=True)
    value = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField('Ativo', default=True)
    photo = models.ImageField('Foto', upload_to='projects/', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Proprietário',
        on_delete=models.CASCADE,
        related_name='projects'
    )

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_tasks_count(self):
        return self.tasks.count()

    def get_status_summary(self):
        todo = self.tasks.filter(status='todo').count()
        doing = self.tasks.filter(status='doing').count()
        done = self.tasks.filter(status='done').count()
        return f"A fazer: {todo}, Em andamento: {doing}, Concluídas: {done}" 