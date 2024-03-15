from django.db import models

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