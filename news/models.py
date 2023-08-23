from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import datetime


class News(models.Model):
    """Модель новостей игры"""
    title = models.CharField(max_length=80, null=False, blank=False,
                             verbose_name='Название новости')
    short_description = models.CharField(max_length=80, null=False, blank=False,
                                         verbose_name="Краткое описание новости")
    full_description = models.CharField(max_length=300, null=False, blank=False,
                                        verbose_name="Полное описание новости")
    trailer = models.URLField(null=True, blank=True, verbose_name="Трейлер")
    date = models.DateTimeField(default=datetime.now(), blank=False, verbose_name="Дата публикации")

    images = models.ImageField(upload_to='games/news/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                               verbose_name='Изображение')

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f'{self.title}'
