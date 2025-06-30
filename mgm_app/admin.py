from django.contrib import admin

# Register your models here.
from .models import Usuarios, Condimentos, Recetas

admin.site.register(Usuarios)
admin.site.register(Condimentos)    
admin.site.register(Recetas)