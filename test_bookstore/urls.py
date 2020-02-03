"""test_bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('test_bookstore_app/', include('test_bookstore_app.urls')),
=======
from django.urls import include, path

urlpatterns = [
    path('testBookstore/', include('test_bookstore_app.urls')),
>>>>>>> a925a115da70cc2336f4b92d1ad23146a2a69702
    path('admin/', admin.site.urls),
]
