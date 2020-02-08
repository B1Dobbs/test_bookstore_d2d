from django.contrib import admin
# Register your models here.

from .models import AuthorsList, Book, Library

admin.site.register(Book)
admin.site.register(AuthorsList)
admin.site.register(Library)
