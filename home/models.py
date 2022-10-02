from unittest.util import _MAX_LENGTH
from django.db import models

from libmanagement.settings import AUTH_PASSWORD_VALIDATORS

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=250)
    isbn = models.CharField(max_length=10)
    publisher = models.CharField(max_length=250)

    def __str__(self):
        return self.title + " " + self.authors + " " +  self.isbn + " " +  self.publisher

class Members(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name