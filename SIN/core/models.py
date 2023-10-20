from django.db import models

# Create your models here.
class Entidad(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre = models.CharField(max_length=30)
    logo = models.ImageField()

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key = True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=500)
    detalle_corto = models.CharField(max_length=300)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField()
    fecha_ultima_publicacion = models.DateTimeField()
