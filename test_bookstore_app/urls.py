from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('library/', views.library, name='library'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
]