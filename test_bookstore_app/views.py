from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from .models import Book
from django.db.models import Q

def book_list(request):
    return HttpResponse("Hello, you are on the book list page")

def book_detail(request):
    title = "Harry Potter and the Sorcerer's Stone"
    author = "J.K. Rowling"
    price = "$11.69"
    release_date = "June 26, 1997"
    isbn = "9780590353427"
    availability = False
    description = "Harry Potter has never been the star of a Quidditch team, scoring points while riding a broom far above the ground. He knows no spells, has never helped to hatch a dragon, and has never worn a cloak of invisibility. All he knows is a miserable life with the Dursleys, his horrible aunt and uncle, and their abominable son, Dudley -- a great big swollen spoiled bully. Harry's room is a tiny closet at the foot of the stairs, and he hasn't had a birthday party in eleven years. But all that is about to change when a mysterious letter arrives by owl messenger: a letter with an invitation to an incredible place that Harry -- and anyone who reads about him -- will find unforgettable."
    series = "Harry Potter"
    volume_number = "2"
    book_id = "9780590353427"

    template = loader.get_template('book_detail.html')
    context = {
        'title' : title,
        'author' : author,
        'price' : price,
        'release_date' : release_date,
        'isbn' : isbn,
        'availability' : availability,
        'description' : description,
        'series' : series,
        'volume_number' : volume_number,
        'book_id' : book_id
    }
    return HttpResponse(template.render(context, request))


from .models import Book
def library(request):
    template = loader.get_template('test_bookstore_app_templates/library.html')
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))

class BookDetailView(DetailView):
    model = Book
    template = loader.get_template('test_bookstore_app/book_detail.html')
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context = {'book': book}
        return render(request, 'test_bookstore_app/book_detail.html', context)

class SearchResultsView(ListView):
    model = Book
    template_name = 'test_bookstore_app/search_results.html'    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(isbn__icontains=query)
        )
        return object_list

