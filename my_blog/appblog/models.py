from django.db import models

# Create your models here.

class Post(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    categorie_id = models.ForeignKey('Categorie', on_delete = models.CASCADE, related_name='categorie_post')

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

