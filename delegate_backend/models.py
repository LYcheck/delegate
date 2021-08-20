from django.db import models

# Create your models here.
class ListItem(models.Model):
    category = models.CharField(max_length=255)
    title = models.TextField(max_length=255)
    