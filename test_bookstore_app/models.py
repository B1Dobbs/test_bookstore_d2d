from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

    
# Create your models here.

class AuthorsList(models.Model):
    name = models.CharField(max_length=250)
    
class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=250)
    authors = models.ForeignKey(AuthorsList, on_delete=models.CASCADE)
    price = models.FloatField()
    release_date = models.DateTimeField('release date')
    availability = models.BooleanField()
    description = models.CharField(max_length=1024)
    series = models.CharField(max_length=250)
    vol_num = models.IntegerField()


class Library(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
