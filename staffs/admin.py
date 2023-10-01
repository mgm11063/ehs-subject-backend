from django.contrib import admin
from .models import Staff, SegType


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(SegType)
class SegTypeAdmin(admin.ModelAdmin):
    pass
