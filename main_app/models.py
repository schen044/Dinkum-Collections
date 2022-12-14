from django.db import models
from django.urls import reverse

# Create your models here.
class Licence(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('licences_detail', kwargs={'pk': self.id})


class User(models.Model):
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    licences = models.ManyToManyField(Licence)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('users_detail', kwargs={'user_id': self.id})
        

class Fish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    time_active = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})