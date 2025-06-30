from django.shortcuts import render
from .models import Usuarios, Condimentos, Recetas
from .forms import UsuariosForm
from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here
def inicio(request):
    busqueda = request.GET.get("Busqueda de usuarios", "")
    if busqueda:
        usuarios = Usuarios.objects.filter(
            Q(nombre__icontains=busqueda) | Q(apellido__icontains=busqueda)
        )
    else:
        usuarios = []

    return render(request, 'mgm_app/inicio.html', {
        'usuarios': usuarios,
        'busqueda': busqueda
    })

def recetas(request):
    recetas = Recetas.objects.all()
    return render(request, 'mgm_app/recetas.html', context={'recetas': recetas})


def usuario_creacion(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mgm_app:usuarios')
    else:
        form = UsuariosForm()
    
    return render(request, 'mgm_app/usuario_creacion.html', {'form': form})

def usuarios(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        usuarios = Usuarios.objects.filter(nombre__icontains=busqueda)
    else:
        usuarios = Usuarios.objects.all()
    return render(request, 'mgm_app/usuarios.html', {'usuarios': usuarios})


def condimentos(request):
    condimentos = Condimentos.objects.all()
    return render(request, 'mgm_app/condimentos.html', context={'condimentos': condimentos})