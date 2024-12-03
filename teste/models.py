from django.db import models


class NumberInput(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)


from django.db import models

class InputModel(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)  # Campo de texto
    email = models.EmailField(blank=True, null=True)  # Campo de e-mail
    password = models.CharField(max_length=255, blank=True, null=True)  # Campo de senha
    date = models.DateField(blank=True, null=True)  # Campo de data
    number = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Campo numérico
    textarea = models.TextField(blank=True, null=True)  # Campo de texto multilinha
    is_active = models.BooleanField(default=False)  # Campo booleano (checkbox)
    category = models.CharField(
        max_length=50, 
        choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')],
        blank=True, 
        null=True
    )  # Campo dropdown

