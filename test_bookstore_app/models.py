from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=250, blank=True)
    authors = models.CharField(max_length=250, blank=True)
    price = models.FloatField(default=0.00)
    release_date = models.DateField('release date', null=True)
    availability = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, blank=True)
    series = models.CharField(max_length=250, blank=True)
    vol_num = models.IntegerField(null=True, blank=True)
    languages = models.CharField(max_length=20, default='eng')

    def __str__(self):
        return self.title + " (" + self.isbn + ")"


class Library(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
