from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic_name = models.CharField(max_length=100, verbose_name="Отчество")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.PositiveBigIntegerField(verbose_name="Телефон")
    birthday = models.DateField(verbose_name="Дата рождения")