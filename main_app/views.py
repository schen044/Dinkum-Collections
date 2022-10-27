from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, User, Licence
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
  id_list = user.licences.all().values_list('id')
  licences_user_doesnt_have = Licence.objects.exclude(id__in=id_list)
  fish_form = FishForm()          
  return render(request, 'user/detail.html', { 'user':user, 'fish_form': fish_form, 'licences': licences_user_doesnt_have })

class UserCreate(CreateView):
  model = User
  fields = '__all__'

class UserUpdate(UpdateView):
  model = User
  fields = '__all__'

class UserDelete(DeleteView):
  model = User
  success_url = '/user/'

# add fish through user detail page
def add_fish(request, user_id):
  form = FishForm(request.POST)
  if form.is_valid():
    new_fish = form.save(commit=False)
    new_fish.user_id = user_id
    new_fish.save()
  return redirect('user_detail', user_id=user_id)

def assoc_licence(request, user_id, licence_id):
  User.objects.get(id=user_id).licences.add(licence_id)
  return redirect('user_detail', user_id=user_id)

class LicenceList(ListView):
  model = Licence

class LicenceDetail(DetailView):
  model = Licence

class LicenceCreate(CreateView):
  model = Licence
  fields = '__all__'

class LicenceUpdate(UpdateView):
  model = Licence
  fields = ['name', 'level']

class LicenceDelete(DeleteView):
  model = Licence
  success_url = '/licences/'