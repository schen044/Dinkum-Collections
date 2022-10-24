from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for fish index
  path('fish/', views.fish_index, name='index'),
  path('fish/<int:fish_id>', views.fish_detail, name='detail'),
]