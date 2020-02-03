from django.urls import path
<<<<<<< HEAD

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_detail', views.book_detail, name='book_detail'),
=======
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
>>>>>>> a925a115da70cc2336f4b92d1ad23146a2a69702
]