from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Book
from django.core.paginator import *

# Create your views here.
def library(request):
    template = loader.get_template('library.html')
    sort = request.GET.get('sort', 'title')
    desc = sort[0]
    book_list = Book.objects.all().order_by(sort)

    paginator = Paginator(book_list, 2)
    page = request.GET.get('page')
    book_list = paginator.get_page(page)
    context = {
        'book_list': book_list,
        'desc': desc,
    }
    return HttpResponse(template.render(context, request))

class BookDetailView(DetailView):
    model = Book
    template = loader.get_template('book_detail.html')
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context = {'book': book}
        return render(request, 'test_bookstore_app/book_detail.html', context)