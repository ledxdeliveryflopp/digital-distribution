from django.db import models


class LanguageText(models.Model):
    """Модель языков текста"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Язык')

    class Meta:
        verbose_name = "Язык текста"
        verbose_name_plural = "Языки текста"

    def __str__(self):
        return f'{self.title}'


class LanguageVoice(models.Model):
    """Модель языков озвучки"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Язык')

    class Meta:
        verbose_name = "Язык озвучки"
        verbose_name_plural = "Языки озвучки"

    def __str__(self):
        return f'{self.title}'


class LanguageSubtitles(models.Model):
    """Модель языков субтитров"""
    title = models.CharField(max_length=80, null=False, blank=False, verbose_name='Язык')

    class Meta:
        verbose_name = "Язык субтитров"
        verbose_name_plural = "Языки субтитров"

    def __str__(self):
        return f'{self.title}'
