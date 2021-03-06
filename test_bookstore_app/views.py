from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Book, Library
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import *
# Create your views here.
def library(request):
    #Book.objects.all().delete()
    template = loader.get_template('library.html')
    try:
        lib = Library.objects.get(pk=1)
    except Library.DoesNotExist:
        lib = Library(1, '')
        lib.save()

    # Get Sorting parameters for context
    sort = request.GET.get('sort', 'title')
    desc = sort[0]

    if request.method == 'GET':
        if 'q' in request.GET:
            lib.search = request.GET['q']
            lib.save()

    # Perform search query on list
    if request.method == 'POST':
        lib.search = request.POST.get('q', '')
        lib.save()
    query = lib.search
    book_list = Book.objects.filter(
            Q(title__icontains=query) | Q(isbn__icontains=query ) | Q(authors__icontains=query)
        ).order_by(sort)

    # Paginate the list
    paginator = Paginator(book_list, 10)
    page = request.GET.get('page', '1')
    book_list = paginator.get_page(page)
    context = {
        'book_list': book_list,
        'desc': desc,
        'q': query,
        'page': page,
    }
    return HttpResponse(template.render(context, request))

class BookDetailView(DetailView):
    model = Book
    template = loader.get_template('book_detail.html')
    
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context = {'book': book}
        return render(request, 'book_detail.html', context)

class SearchResultsView(ListView):
    model = Book
    template_name = 'library.html'    
    def get_queryset(self):
        query = self.request.GET.get('q')
        sort = self.request.GET.get('sort', 'title')
        desc = sort[0]
        searchReq = query
        book_list = Book.objects.filter(
            Q(title__icontains=query) | Q(isbn__icontains=query ) | Q(authors__icontains=query)
        ).order_by(sort)
        return book_list
