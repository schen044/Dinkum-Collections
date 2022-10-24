from django.db import models

# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time_active = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    price = models.IntegerField()