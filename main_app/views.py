from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, User

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

## USER VIEWS ##
def user_index(request):
  users = User.objects.all()
  return render(request, 'user/index.html', { 'users': users })

def user_detail(request, user_id):
  user = User.objects.get(id=user_id)
  return render(request, 'user/detail.html', { 'user':user })