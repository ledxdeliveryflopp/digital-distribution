from django.db import models


class Tags(models.Model):
    """Модель меток"""
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название метки")

    class Meta:
        verbose_name = "Метка"
        verbose_name_plural = "Метки"

    def __str__(self):
        return f'{self.title}'
