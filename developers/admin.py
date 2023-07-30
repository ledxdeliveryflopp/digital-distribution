from django.contrib import admin
from .models import DeveloperCompany


@admin.register(DeveloperCompany)
class DeveloperCompanyAdmin(admin.ModelAdmin):
    pass
