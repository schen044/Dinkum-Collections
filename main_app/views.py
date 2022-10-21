from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Fish:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, location, time_active, season, price):
    self.name = name
    self.location = location
    self.time_active = time_active
    self.season = season
    self.price = price

fish = [
  Fish('Anchovy', 'Southern Ocean', 'day, night', 'Fall, Winter', 4520),
  Fish('Banded Morwong', 'Northern Ocean, Southern Ocean', 'day, noon, night', 'Winter', 4320),
  Fish('Barcoo Grunter', 'Rivers, Billabongs, Mangroves', 'day, noon, night', 'Spring, Summer, Fall, Winter', 1290)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def fish_index(request):
  return render(request, 'fish/index.html', { 'fish': fish })
