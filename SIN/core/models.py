from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Departamentos
class Entidad(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre = models.CharField(max_length=30, help_text="Ingrese el nombre del departamento")
    logo = models.ImageField(help_text="Añada el logo del departamento")
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"




#Comunicados
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key = True)
    titulo = models.CharField(max_length=50, help_text="Ingrese el titulo del comunicado")
    detalle = models.TextField()
    detalle_corto = models.CharField(max_length=300)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, help_text="Elija el departamento asociado")
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    TIPO_CHOICES = [
    ("-", "Seleccionar"),
    ("S", "Suspensión de actividades"),
    ("C", "Suspensión de clases"),
    ("I", "Información"),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="-")
    publicado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="publicado_por")
    modificado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="modificado_por")


    def __str__(self):
        return self.titulo
