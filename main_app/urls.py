from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  ## ROUTES FOR FISH ##
  path('fish/', views.fish_index, name='index'),
  path('fish/<int:fish_id>', views.fish_detail, name='detail'),
  path('fish/create/', views.FishCreate.as_view(), name='fish_create'),
  path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
  path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
  ## ROUTES FOR USER ##
  path('user/', views.user_index, name='user_index'),
  path('user/<int:user_id>', views.user_detail, name='user_detail'),
]