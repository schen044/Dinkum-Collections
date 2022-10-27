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
  path('users/', views.users_index, name='users_index'),
  path('users/<int:user_id>', views.users_detail, name='users_detail'),
  path('users/create/', views.UserCreate.as_view(), name='users_create'),
  path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='users_update'),
  path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='users_delete'),
  path('users/<int:user_id>/add_fish/', views.add_fish, name='add_fish'),
  path('users/<int:user_id>/assoc_licence/<int:licence_id>/', views.assoc_licence, name='assoc_licence'),
  ## ROUTES FOR LICENCES
  path('licences/', views.LicenceList.as_view(), name='licences_index'),
  path('licences/<int:pk>/', views.LicenceDetail.as_view(), name='licences_detail'),
  path('licences/create/', views.LicenceCreate.as_view(), name='licences_create'),
  path('licences/<int:pk>/update/', views.LicenceUpdate.as_view(), name='licences_update'),
  path('licences/<int:pk>/delete/', views.LicenceDelete.as_view(), name='licences_delete'),
]