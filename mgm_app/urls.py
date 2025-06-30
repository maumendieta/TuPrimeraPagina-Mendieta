from django.urls import path
from . import views

app_name = 'mgm_app'

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("recetas/", views.recetas, name="recetas"),
    path("condimentos/", views.condimentos, name="condimentos"),
    path("usuarios/creacion/", views.usuario_creacion, name="usuario_creacion"),
]