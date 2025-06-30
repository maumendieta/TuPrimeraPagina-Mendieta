from django.shortcuts import render
from .models import Usuarios, Condimentos, Recetas

# Create your views here
def inicio(request):
    return render(request, 'mgm_app/inicio.html')

def recetas(request):
    return render(request, 'mgm_app/recetas.html')


def usuarios(request):
    return render(request, 'mgm_app/usuarios.html')

def condimentos(request):
    return render(request, 'mgm_app/condimentos.html')