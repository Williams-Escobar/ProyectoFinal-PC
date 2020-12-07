from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 

class Pelicula (models.Model):
    nombre = models.CharField(max_length=80)
    sinopsis = models.CharField(max_length=200)
    anio   = models.CharField(max_length=50)
    productor = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria, related_name='pelicula', on_delete=models.CASCADE) 
    

    def __str__(self):
        return self.nombre