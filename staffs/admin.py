from django.contrib import admin
from .models import Staff, G_examination, S_examination


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(G_examination)
class G_examinationAdmin(admin.ModelAdmin):
    pass


@admin.register(S_examination)
class S_examinationAdmin(admin.ModelAdmin):
    pass
