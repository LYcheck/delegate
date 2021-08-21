from django.db import models

# Create your models here.
class Item(models.Model):
    category = models.CharField(max_length=20)
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title
    
# class List(models.model):
#     title = models.TextField(max_length=255)

# class User(models.model):
#     name = models.TextField(max_length=255)

# class Event(models.model):
#     title = models.TextField(max_length=255)

# class Group(models.model):
#     name = models.TextField(max_length=255)
