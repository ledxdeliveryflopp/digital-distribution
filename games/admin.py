from django.contrib import admin
from .models import Game, Tags, DownloadableContent


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


@admin.register(DownloadableContent)
class DownloadableContentAdmin(admin.ModelAdmin):
    pass

