from django.contrib import admin
from .models import Factor


@admin.register(Factor)
class FactorAdmin(admin.ModelAdmin):
    pass
