from django.shortcuts import render
from .models import Categoria 

def post_list(request):
    return render(request, 'peliculas/base.html', {'publicacion':'publicacion'})

def categorias(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'peliculas/categorias.html', {'categorias':categorias})