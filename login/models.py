from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(default="",max_length=100)
    password=models.charfield(default="",max_length=100)
class Registration(models.Model):
    fullname=models.CharField(default="",max_length=100)
    lastname=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)
    phone=models.CharField(default="",max_length=100)
    email=models.CharField(default="",max_length=100)
