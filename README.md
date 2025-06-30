# TuPrimeraPagina-Mendieta
## Trabajo Coderhouse
### Tercera Entrega


## Pasos Creación de Repositorio 🔧
1- Crear Repositorio Git
2- git clone (CTRL V)


## Pasos para actualizar repositorio ⚙️
1- git add . 
2- git commit -m "mensaje"
3- git push


## Activar entorno virtual: 🛠️
1- python -m venv .venv (creación de entorno virtual)
2- ejecutar el Script activate del .venv: .\.venv\Scripts\activate
**********************************************************
SI EL SISTEMA TIRA ALGUN ERROR O ADVERTENCIA DE WIONDOWS POR PELIGROSIDAD, ejecutar desde POWER SHELL (Como administrador), el siguiente comando:
Set-ExecutionPolicy Unrestricted
-Elegir Opción YES- 
***********************************************************
3- instalar DJANGO en el entorno virtual: pip install django


## Primeros pasos en DJANGO 😁
- Comandos: django-admin
- PARA CREAR PROYECTO USAMOS: django-admin startproject NombreProyecto . (espacio punto es para que no cree una nueva carpeta)
- Ese comando crea un archivo llamado manage.py que sirve para administrar el proyecto.
- Para iniciar el servidor se debe ejecutar el comando: python manage.py runserver
*****************************************************
FRENAR EL SERVIDOR > CRTL + C
*****************************************************

## CREACION DE APLICACION ☑️
1- dentro del entorno virtual .venv, se debe crear la aplicación.
2- python manage.py startapp NombreApp
APENAS CREAMOS LA APLICACIÓN DEBEMOS REGISTRARLA EN NombreProyecto/SETTINGS.py
Se agrega en el siguiente listado:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 ###   'mgm_app', # registro de apliación personalizada creada por mgm #]


## Creación de Templates
En el contexto digital, un template o plantilla es un archivo o diseño predefinido que sirve como base para la creación de otros documentos, páginas web, o elementos visuales. Permite estandarizar la apariencia y estructura, facilitando la creación de contenido nuevo de manera consistente y eficiente.

Se crean dentro de la carpeta Nombre_App


## CREACION DE MODELOS (Clases)
Iniciar instancia de shell dentro de la consola de django
python manage.py shell
(se usa para poder crear datos en la clase creada)

Para poder guardar los datos desde la consola class.save() , chat gpt, ante un error de guardado me sugirió:

1. python manage.py makemigrations
#Este comando generará las migraciones necesarias (archivos .py que definen cómo crear/modificar tablas en la base de datos).
2. python manage.py migrate
Este aplicará las migraciones, es decir, creará la tabla mgm_app_usuarios (y todas las que falten) en tu base de datos SQLite (o la que estés usando).

Luego de correr esos dos comandos desde  desde la raíz del  proyecto (fuera del shell), pude guardar perfectamente.

*******************************************************************
ANTE UNA MODIFICACIÓN DE LA BASE DE DATOS ES IMPORTANTE EJECUTAR
python manage.py makemigrations
*******************************************************************