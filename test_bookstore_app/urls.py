from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
<<<<<<< HEAD
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    
=======
>>>>>>> 5f28351429969eca77cb9c4ff5aa02e7a85f2a75
]