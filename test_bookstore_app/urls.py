from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    
]