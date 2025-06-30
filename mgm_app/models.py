from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Condimentos(models.Model):
    fracciones = [
        ('litros', 'Litros'),
        ('gramos', 'Gramos'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo_condimento = models.CharField(max_length=50)
    fraccion = models.CharField(max_length=20, choices= fracciones)

    def __str__(self):
        return f"{self.nombre}"
    

class Recetas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo_receta = models.CharField(max_length=50)
    complejidad = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}"