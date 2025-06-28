from django.shortcuts import render

# Create your views here
def index(request):
    context = {"mensaje": "BIENVENIDOS!"}
    return render(request, 'mgm_app/index.html', context)