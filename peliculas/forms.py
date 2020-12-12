from django import forms

from .models import Pelicula

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ('nombre', 'sinopsis','anio','productor','categoria',)