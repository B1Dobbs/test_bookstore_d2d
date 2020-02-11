from django.contrib import admin

# Register your models here.
from .models import Book, Library

admin.site.register(Book)
admin.site.register(Library)