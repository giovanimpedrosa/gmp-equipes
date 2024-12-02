from django.db import models


class NumberInput(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
