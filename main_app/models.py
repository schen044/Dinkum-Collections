from django.db import models
from django.urls import reverse

# Create your models here.
class Museum(models.Model):
    town_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.town_name}'s Museum"
        
class Fish(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time_active = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    price = models.IntegerField()
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})