from django.core.validators import MinValueValidator
from django.db import models

class Revenue(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата и время")
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    driver = models.ForeignKey("drivers.Driver", on_delete=models.CASCADE, verbose_name="Водитель")