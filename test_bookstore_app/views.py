from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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


