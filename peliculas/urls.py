from django.urls import path
from . import views

urlpatterns = [
   path('', views.pelicula_list, name='pelicula_list'),
   path('newPelicula', views.create_pelicula, name='create_pelicula'),
]