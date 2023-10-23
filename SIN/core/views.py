from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad

# Create your views here.
def index(request):
    title = "Inicio"
    entidad = Entidad.id
    numComunicados = Comunicado.objects.filter(visible = True).count()
    
    data = {
        "title": title,
        "numComunicados": numComunicados,
        "entidad": entidad,
    }

    return render(request, 'core/index.html', data)