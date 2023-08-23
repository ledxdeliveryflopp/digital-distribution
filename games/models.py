from datetime import datetime, timedelta
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
from developers.models import DeveloperCompany
from dls.models import DownloadableContent
from language.models import LanguageText, LanguageSubtitles, LanguageVoice
from news.models import News
from region.models import Region
from tags.models import Tags


class Game(models.Model):
    """Модель игры"""
    title = models.CharField(max_length=80, verbose_name='Название игры')
    short_description = models.CharField(max_length=80, verbose_name="Краткое описание игры")
    full_description = models.CharField(max_length=300, verbose_name="Полное описание игры")
    price = models.IntegerField(default=1000, verbose_name="Цена игры")
    sale = models.BooleanField(default=False, verbose_name="Скидка")
    discount = models.IntegerField(default=0, validators=[MaxValueValidator(100)],
                                   verbose_name="Процент скидки")
    price_discount = models.IntegerField(default=0, verbose_name="Цена игры со скидкой")
    min_system_requirements = models.CharField(max_length=150,
                                               verbose_name="Минимальные системные требования")
    req_system_requirements = models.CharField(max_length=150,
                                               verbose_name="Рекомендуемые системные требования")
    release_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата выхода")
    New_game_date = models.DateTimeField(default=datetime.now() + timedelta(days=10),
                                         verbose_name="Срок новинки")
    new_game = models.BooleanField(default=False, verbose_name="Новинка")

    region = models.ManyToManyField(Region, blank=False, verbose_name="Регион", related_name="games")
    mews = models.ManyToManyField(News, blank=True, verbose_name="Новости игры", related_name="game")
    language_text = models.ManyToManyField(LanguageText, blank=False, verbose_name="Язык текста")
    language_voice = models.ManyToManyField(LanguageVoice, blank=False, verbose_name="Язык озвучки")
    language_subtitles = models.ManyToManyField(LanguageSubtitles, blank=False,
                                                verbose_name="Язык субтитров")
    downloadable_content = models.ManyToManyField(DownloadableContent, blank=True,
                                                  verbose_name="Загружаемый контент",
                                                  related_name='game')
    tags = models.ManyToManyField(Tags, blank=False, verbose_name="Метки", related_name="games")
    developer = models.ForeignKey(DeveloperCompany, on_delete=models.CASCADE, null=False,
                                  blank=False, verbose_name="Компания разработчик",
                                  related_name="games")

    title_image = models.ImageField(upload_to='games/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                            verbose_name='Титульное изображение')
    images = models.ImageField(upload_to='games/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                            verbose_name='Изображение')
    trailer = models.URLField(null=True, blank=True, verbose_name="Трейлер")

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def save(self, *args, **kwargs):
        if self.sale and self.price > 100 and self.New_game_date.date() > self.release_date.date():
            self.price_discount = (self.price * (100 - self.discount) / 100)
            self.new_game = True
        elif self.sale and self.price > 100 and self.New_game_date.date() < self.release_date.date():
            self.price_discount = (self.price * (100 - self.discount) / 100)
            self.new_game = False
        elif not self.sale  and self.price > 100 and self.New_game_date.date() > self.release_date.date():
            self.price_discount = (self.price * (100 - self.discount) / 100)
            self.new_game = True
        elif not self.sale and self.price > 100 and self.New_game_date.date() < self.release_date.date():
            self.price_discount = (self.price * (100 - self.discount) / 100)
            self.new_game = False
        else:
            self.sale = False
            self.new_game = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

