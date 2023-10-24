from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad

# Create your views here.
def index(request):
    title = "Inicio"
    comunicados = Comunicado.objects.all()
    entidades = list(Entidad.objects.all())
    filtro = request.POST.get("departamento")
    if filtro == None:
        filtro = "Departamentos"
    if filtro in entidades:
        comunicados = Comunicado.objects.filter(entidad=filtro)
    else:
        comunicados = Comunicado.objects.all()
    data = {
        "title": title,
        "comunicados": comunicados, 
        "entidades": entidades,
        "filtro": filtro,
    }

    return render(request, 'core/index.html', data)
