from django.urls import path
from . import views

urlpatterns = [
   path('', views.post_list, name='post_list'),
   path('categorias/', views.categorias, name='categorias'),
   path('categorias/nuevo', views.categoria_nuevo, name='categoria_nuevo'),
   path('categoria/<int:pk>/edit/', views.categoria_edit, name='categoria_edit'),
   path('categoria/<int:pk>/delete/', views.categoria_delete, name='categoria_delete'),
]
