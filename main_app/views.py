from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish, User
from .forms import FishForm

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
  fields = '__all__'

class FishDelete(DeleteView):
  model = Fish
  success_url = '/fish/'

## USER VIEWS ##
def user_index(request):
  users = User.objects.all()
  return render(request, 'user/index.html', { 'users': users })

def user_detail(request, user_id):
  user = User.objects.get(id=user_id)
  fish_form = FishForm()          
  return render(request, 'user/detail.html', { 'user':user, 'fish_form': fish_form})

class UserCreate(CreateView):
  model = User
  fields = '__all__'

# add fish through user detail page
def add_fish(request, user_id):
  form = FishForm(request.POST)
  if form.is_valid():
    new_fish = form.save(commit=False)
    new_fish.user_id = user_id
    new_fish.save()
  return redirect('user_detail', user_id=user_id)
