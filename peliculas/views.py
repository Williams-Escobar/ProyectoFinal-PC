from django.shortcuts import render

def post_list(request):
    return render(request, 'peliculas/base.html', {'publicacion':'publicacion'})
