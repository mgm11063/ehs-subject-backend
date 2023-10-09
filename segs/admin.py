from django.contrib import admin
from .models import Factor, Seg


@admin.register(Factor)
class FactorAdmin(admin.ModelAdmin):
    pass


@admin.register(Seg)
class SegAdmin(admin.ModelAdmin):
    pass
