from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
<<<<<<< HEAD
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
=======

def book_list(request):
    return HttpResponse("Hello, you are on the book list page")

def book_detail(request):
    title = "Harry Potter and the Sorcerer's Stone"
    author = "J.K. Rowling"
    price = "$11.69"
    release_date = "June 26, 1997"
    isbn = "9780590353427"
    availability = "for sale"
    description = "Harry Potter has never been the star of a Quidditch team, scoring points while riding a broom far above the ground. He knows no spells, has never helped to hatch a dragon, and has never worn a cloak of invisibility."
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


>>>>>>> 5f28351429969eca77cb9c4ff5aa02e7a85f2a75
from .models import Book
def library(request):
    template = loader.get_template('test_bookstore_app/library.html')
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))
<<<<<<< HEAD

class BookDetailView(DetailView):
    model = Book
    template = loader.get_template('test_bookstore_app/book_detail.html')
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context = {'book': book}
        return render(request, 'books/book_detail.html', context)
=======
>>>>>>> 5f28351429969eca77cb9c4ff5aa02e7a85f2a75
