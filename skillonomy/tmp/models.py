from django.db import models


class Mentor(models.Model):
    name= models.CharField(max_length=255)
    rating = models.IntegerField(default=0,  blank=True)

class Curs(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="tmp/static/tmp/img", blank=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %self.image



class User(models.Model):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=255)
    curs = models.ManyToManyField(Curs)
    balance = models.FloatField(default=0, )
    creator = models.CharField(max_length=255, blank=True)

