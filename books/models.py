from django.db import models

# Create your models here.
class BookModel(models.Model):
    title=models.CharField(default="",max_length=100)
    Author=models.CharField(default='',max_length=100)
    genre=models.CharField(default='',max_length=100)
    image=models.CharField(default='',max_length=1000)
    publishedby=models.CharField(default='',max_length=100)
    price=models.CharField(default="",max_length=100)