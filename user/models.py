from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from games.models import Game
from region.models import Region


class User(AbstractUser):
    """Модель пользователя"""
    username = models.CharField(max_length=20, null=False, blank=False, unique=True,
                                validators=[UnicodeUsernameValidator],
                                verbose_name="Имя пользователя")
    description = models.CharField(max_length=200, null=True, blank=True,
                                   verbose_name="Описание профиля")

    games = models.ManyToManyField(Game, blank=True, verbose_name="Игры на аккаунте")
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL, verbose_name="Регион")

    avatar = models.ImageField(upload_to='avatar', default='avatar/default.png', null=True,
                               blank=True, verbose_name="Аватарка пользователя")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return f'{self.username}'
