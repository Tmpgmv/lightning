from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic_name = models.CharField(max_length=100, verbose_name="Отчество")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.PositiveBigIntegerField(verbose_name="Телефон")
    birthday = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic_name}"
