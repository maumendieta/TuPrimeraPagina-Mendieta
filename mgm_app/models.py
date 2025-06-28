from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def save(self):
        print("Guardando usuario...")
        super().save()
