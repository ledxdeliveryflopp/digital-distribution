from django.core.validators import MaxValueValidator, FileExtensionValidator
from django.db import models
from developers.models import DeveloperCompany
from language.models import LanguageText, LanguageSubtitles, LanguageVoice
from tags.models import Tags


class DownloadableContent(models.Model):
    """Модель загружаемого контента"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Название DLS')
    short_description = models.CharField(max_length=80, null=False, blank=False, verbose_name="Краткое описание DLS")
    full_description = models.CharField(max_length=300, null=False, blank=False, verbose_name="Полное описание DLS")
    price = models.IntegerField(default=0, null=False, blank=False, verbose_name="Цена DLS")
    sale = models.BooleanField(default=False, null=False, blank=False, verbose_name="Скидка")
    discount = models.IntegerField(default=0, null=False, blank=False, validators=[MaxValueValidator(100)],
                                   verbose_name="Процент скидки")
    price_discount = models.IntegerField(default=0, null=False, blank=False, verbose_name="Цена DLS со скидкой")
    min_system_requirements = models.CharField(max_length=150, null=False, blank=False,
                                               verbose_name="Минимальные системные требования")
    req_system_requirements = models.CharField(max_length=150, null=False, blank=False,
                                               verbose_name="Рекомендуемые системные требования")
    release_date = models.DateField(null=False, blank=False, verbose_name="Дата выхода")

    language_text = models.ManyToManyField(LanguageText, blank=False, verbose_name="Язык текста")
    language_voice = models.ManyToManyField(LanguageVoice, blank=False, verbose_name="Язык озвучки")
    language_subtitles = models.ManyToManyField(LanguageSubtitles, blank=False, verbose_name="Язык субтитров")
    tags = models.ManyToManyField(Tags, blank=False, verbose_name="Метки", related_name='dls')
    developer = models.ForeignKey(DeveloperCompany, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name="dls")

    title_image = models.ImageField(upload_to='games/dls/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                                    verbose_name='Титульное изображение')
    images = models.ImageField(upload_to='games/dls/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                            verbose_name='Изображение')
    trailer = models.URLField(null=True, blank=True, verbose_name="Трейлер")

    class Meta:
        verbose_name = "Загружаемый контент"
        verbose_name_plural = "Загружаемый контент"

    def save(self, *args, **kwargs):

        if self.sale and self.price > 100:
            self.price_discount = (self.price * (100 - self.discount) / 100)
        else:
            self.sale = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

