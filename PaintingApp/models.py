from django.db import models

# Create your models here.
class Painting(models.Model):
    ID = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length=200)
    Artist = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Price = models.IntegerField(max_length=10000)