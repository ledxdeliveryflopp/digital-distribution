from django.contrib import admin
from .models import DownloadableContent


@admin.register(DownloadableContent)
class DownloadableContentAdmin(admin.ModelAdmin):
    readonly_fields = ['price_discount']
