from datetime import datetime, timedelta
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
from developers.models import DeveloperCompany


class Game(models.Model):
    """Модель игры"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Название игры')
    short_description = models.CharField(max_length=80, null=False, blank=False, verbose_name="Краткое описание игры")
    full_description = models.CharField(max_length=300, null=False, blank=False, verbose_name="Полное описание игры")
    price = models.IntegerField(default=1000, null=False, blank=False, verbose_name="Цена игры")
    sale = models.BooleanField(default=False, null=False, blank=False, verbose_name="Скидка")
    discount = models.IntegerField(default=0, null=False, blank=False, validators=[MaxValueValidator(100)],
                                   verbose_name="Процент скидки")
    price_discount = models.IntegerField(default=0, null=False, blank=False, verbose_name="Цена игры со скидкой")
    min_system_requirements = models.CharField(max_length=150, null=False, blank=False,
                                               verbose_name="Минимальные системные требования")
    req_system_requirements = models.CharField(max_length=150, null=False, blank=False,
                                               verbose_name="Рекомендуемые системные требования")
    release_date = models.DateTimeField(default=datetime.now(), blank=False, verbose_name="Дата выхода")
    # language = models.CharField(max_length=10, null=False, blank=False, verbose_name="Цена игры")
    # comments = models.CharField(max_length=10, null=False, blank=False, verbose_name="Цена игры")
    new_game = models.BooleanField(default=False, null=False, blank=False, verbose_name="Новинка")
    New_game_date = models.DateTimeField(default=datetime.now() + timedelta(days=10), blank=False, verbose_name="Дата выхода")

    downloadable_content = models.ManyToManyField("DownloadableContent", blank=True, verbose_name="Загружаемый контент",
                                                  related_name='game')
    tags = models.ManyToManyField("Tags", blank=False, verbose_name="Метки", related_name="games")
    developer = models.ForeignKey(DeveloperCompany, on_delete=models.CASCADE, null=False, blank=False,
                                  verbose_name="Компания разработчик", related_name="games")

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
        elif self.sale == False and self.price > 100 and self.New_game_date.date() > self.release_date.date():
            self.price_discount = (self.price * (100 - self.discount) / 100)
            self.new_game = True
        elif self.sale == False and self.price > 100 and self.New_game_date.date() < self.release_date.date():
            self.price_discount = (self.price * (100 - self.discount) / 100)
            self.new_game = False
        else:
            self.sale = False
            self.new_game = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Tags(models.Model):
    """Модель меток"""
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название метки")

    class Meta:
        verbose_name = "Метка"
        verbose_name_plural = "Метки"

    def __str__(self):
        return f'{self.title}'


class DownloadableContent(models.Model):
    """Модель загружаемого контента"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Название DLS')
    short_description = models.CharField(max_length=80, null=False, blank=False, verbose_name="Краткое описание DLS")
    full_description = models.CharField(max_length=300, null=False, blank=False, verbose_name="Полное описание DLS")
    price = models.IntegerField(default=0, null=False, blank=False, verbose_name="Цена DLS")
    sale = models.BooleanField(default=False, null=False, blank=False, verbose_name="Скидка")
    discount = models.IntegerField(default=0, null=False, blank=False, validators=[MaxValueValidator(100)],
                                   verbose_name="Процент скидки")
    price_discount = models.IntegerField(default=0, null=False, blank=False, verbose_name="Цена игры со скидкой")
    min_system_requirements = models.CharField(max_length=150, null=False, blank=False,
                                               verbose_name="Минимальные системные требования")
    release_date = models.DateField(null=False, blank=False, verbose_name="Дата выхода")
    new_game = models.BooleanField(default=False, null=False, blank=False, verbose_name="Новинка")

    tags = models.ManyToManyField(Tags, blank=False, verbose_name="Метки", related_name='dls')
    developer = models.ForeignKey(DeveloperCompany, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name="dls")

    title_image = models.ImageField(upload_to='games/', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
                                    verbose_name='Титульное изображение')
    images = models.ImageField(upload_to='games/', blank=False, validators=[
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
