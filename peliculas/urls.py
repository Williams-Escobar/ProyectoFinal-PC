from django.urls import path
from . import views

urlpatterns = [
   path('', views.pelicula_list, name='pelicula_list'),
   path('newPelicula', views.create_pelicula, name='create_pelicula'),
   path('edit_pelicula/<int:pk>', views.edit_pelicula, name='edit_pelicula'),
   path('delete_pelicula/<int:pk>', views.delete_pelicula, name='delete_pelicula'),
]