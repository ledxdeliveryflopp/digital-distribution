from django.db import models


class Region(models.Model):
    """Модель региона"""
    title = models.CharField(max_length=30, unique=True, verbose_name="Регион")
    currency = models.CharField(max_length=10, verbose_name="Валюта")

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self) -> str:
        return f'{self.title}'
