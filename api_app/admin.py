from django.contrib import admin
from .models import OnixFile

# Register your models here.

@admin.register(OnixFile)
class FileAdmin(admin.ModelAdmin):
    model = OnixFile
