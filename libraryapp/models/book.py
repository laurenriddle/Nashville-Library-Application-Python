from django.db import models
from .librarian import Librarian
from .library import Library

# this is a class to create a template for all books that will be returned via SQL queries
class Book(models.Model):

    title = models.CharField(max_length = 50)
    ISBN = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)    
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
