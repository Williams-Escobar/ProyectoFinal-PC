from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Pelicula, Categoria
from .forms import PeliculaForm, CategoriaForm

def post_list(request):
    return render(request, 'peliculas/base.html', {'publicacion':'publicacion'})

def categorias(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'peliculas/categorias.html', {'categorias':categorias})

def categoria_nuevo(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()
    return render(request, 'peliculas/categoria_edit.html', {'form': form})

def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'peliculas/categoria_edit.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('categorias')

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
