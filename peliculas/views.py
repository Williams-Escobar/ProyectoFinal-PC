from django.shortcuts import render, get_object_or_404, redirect
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

def edit_pelicula(request,pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        formulario = PeliculaForm(request.POST, instance=pelicula)
        if formulario.is_valid():
            pelicula = formulario.save(commit=False)
            pelicula.save()
            return redirect('pelicula_list')
    else:
        formulario = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/newPelicula.html', {'form': formulario})

def delete_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    pelicula.delete()
    return redirect('pelicula_list')