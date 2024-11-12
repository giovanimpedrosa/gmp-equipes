from django.db import models

# Create your models here.

class TipoProjeto(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Tipo de Projeto"
        verbose_name_plural = "Tipos de Projeto"
        ordering = ['descricao']

    def __str__(self):
        return self.descricao
