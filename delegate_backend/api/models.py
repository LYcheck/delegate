from django.db import models

# Create your models here.
class Item(models.Model):
    class Meta:
        db_table = "Items"
    
    name = models.CharField(max_length=100, default='None')
    type = models.CharField(max_length=50, default='None')
    description = models.CharField(max_length=255, default='None')
    parent_list = models.CharField(max_length=36, default='None')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class List(models.Model):
    class Meta:
        db_table = "Lists"

    name = models.CharField(max_length=100, default='None')
    type = models.CharField(max_length=50, default='None')
    description = models.CharField(max_length=255, default='None')
    author = models.CharField(max_length=36, default='None')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(models.Model):
    class Meta:
        db_table = "Users"

    username = models.TextField(max_length=255, default='None')
    password = models.TextField(max_length=255, default='None')
    email = models.EmailField(max_length=254, default='None')

    def __str__(self):
        return self.username

class Event(models.Model):
    class Meta:
        db_table = "Events"

    name = models.TextField(max_length=255, default='None')
    author = models.CharField(max_length=36, default='None')
    description = models.CharField(max_length=255, default='None')
    parent_list = models.CharField(max_length=36, default='None')
    parent_group = models.CharField(max_length=36, default='None')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    class Meta:
        db_table = "Groupss"
        
    name = models.TextField(max_length=255, default='None')
    author = models.CharField(max_length=36, default='None')
    description = models.CharField(max_length=255, default='None')

    def __str__(self):
        return self.name