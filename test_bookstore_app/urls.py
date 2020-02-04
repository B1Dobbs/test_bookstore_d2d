from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path('book_detail/', views.book_detail, name='book_detail'),
]