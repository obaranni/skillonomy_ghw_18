from django.db import models

class Curs(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="course/", blank=True)

class User(models.Model):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=255)
    curs = models.ManyToManyField(Curs)
    balance = models.FloatField(default=0, )
    creator = models.CharField(max_length=255, blank=True)

class Mentor(models.Model):
    name= models.CharField(max_length=255)
    rating = models.IntegerField()






# Create your models here.
