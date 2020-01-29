from django.shortcuts import render
from django.http import HttpResponse

def book_detail(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''class DetailView(generic.DetailView):
    model = Question
    template_name = 'test_bookstore_app/book-detail.html'''
