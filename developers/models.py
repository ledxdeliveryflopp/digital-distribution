from django.db import models


class DeveloperCompany(models.Model):
    """МОдель компании разработчика"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name="Название компании")
    description = models.CharField(max_length=180, null=True, blank=True, verbose_name="Описание компании")

    class Meta:
        verbose_name = "Компания разработчик"
        verbose_name_plural = "Компании разработчики"

    def __str__(self):
        return f'{self.title}'

