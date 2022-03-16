from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# One to many
class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# One to One
class Person(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    mobile = models.TextField(max_length=100)


class Adhar(models.Model):
    person = models.OneToOneField("Person", on_delete=models.CASCADE)
    signature = models.TextField()
    adhar_no = models.TextField(max_length=100)


# Many to Many

class Movie(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Artists(models.Model):
    name = models.TextField(max_length=100)
    movies = models.ManyToManyField(Movie)
    def __str__(self):
        return self.name
