from django.shortcuts import render
from .models import Categoria 
from .forms import CategoriaForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

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