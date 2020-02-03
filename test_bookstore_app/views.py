from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Book

# Create your views here.
def library(request):
    template = loader.get_template('test_bookstore_app/library.html')
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))