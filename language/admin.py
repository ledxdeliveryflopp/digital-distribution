from django.contrib import admin
from .models import LanguageText, LanguageVoice, LanguageSubtitles


@admin.register(LanguageText)
class LanguageTextAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageVoice)
class LanguageVoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageSubtitles)
class LanguageSubtitlesAdmin(admin.ModelAdmin):
    pass

