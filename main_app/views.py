from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, Museum

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

## FISH VIEWS ##
def fish_index(request):
  fishes = Fish.objects.all()
  return render(request, 'fish/index.html', { 'fishes': fishes })

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render(request, 'fish/detail.html', { 'fish':fish })

class FishCreate(CreateView):
  model = Fish
  fields = '__all__'

class FishUpdate(UpdateView):
  model = Fish
  fields = ['name', 'location', 'time_active', 'season', 'price']

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'

## MUSEUM VIEWS ##
def museum_index(request):
  museums = Museum.objects.all()
  return render(request, 'museum/index.html', { 'museums': museums })

def museum_detail(request, museum_id):
  museum = Museum.objects.get(id=museum_id)
  return render(request, 'museum/detail.html', { 'museum':museum })