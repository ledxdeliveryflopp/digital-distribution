from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    readonly_fields = ['price_discount', 'new_game', 'New_game_date']


