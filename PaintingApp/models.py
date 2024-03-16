from django.db import models
from accounts.models import CustomUser  

class Like(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    painting = models.ForeignKey('PaintingApp.Painting', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'painting')

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    painting = models.ForeignKey('PaintingApp.Painting', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Painting(models.Model):
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Artist = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Price = models.IntegerField()
    image = models.FileField(upload_to='paintings/', null=True, blank=True)  

    
# class Meta:
#     permissions = (
#         ("can_create_painting", "Can create painting"),
#         ("can_edit_painting", "Can edit painting"),
#         ("can_delete_painting", "Can delete painting"),
#     )