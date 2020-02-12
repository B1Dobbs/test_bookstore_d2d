from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Book
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.
def library(request):
    template = loader.get_template('library.html')
    #try:
    book_list = Book.objects.all()
    #except Book.DoesNotExist:
        #raise Http404("No books are in the library")
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))

class BookDetailView(DetailView):
    model = Book
    template = loader.get_template('book_detail.html')
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context = {'book': book}
        return render(request, 'test_bookstore_app/book_detail.html', context)

class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(isbn__icontains=query)
        )
        return object_list