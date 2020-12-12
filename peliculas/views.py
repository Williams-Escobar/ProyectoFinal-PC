from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Pelicula
from .forms import PeliculaForm

def pelicula_list(request):
    peliculas = Pelicula.objects.filter(fecha_Creacion__lte=timezone.now()).order_by('fecha_Creacion')
    return render(request, 'peliculas/listPeliculas.html', {'peliculas':peliculas})

def create_pelicula(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.save()
            return redirect('pelicula_list')
    else:
        formulario = PeliculaForm()
    return render(request, 'peliculas/newPelicula.html', {'form': formulario})