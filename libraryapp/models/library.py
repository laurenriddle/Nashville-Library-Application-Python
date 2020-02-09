from django.db import models

# this is a class to create a template for all libraries that will be returned via SQL queries

class Library(models.Model):

    title = models.CharField(max_length = 50)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.title

