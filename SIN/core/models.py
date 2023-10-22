from django.db import models

# Create your models here.

#Departamentos
class Entidad(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre = models.CharField(max_length=30, help_text="Ingrese el nombre del departamento")
    logo = models.ImageField(help_text="Añada el logo del departamento")

    def __str__(self):
        return self.nombre

TIPO_CHOICES = (
    ("S", "Suspensión de actividades"),
    ("C", "Suspensión de clases"),
    ("I", "Información")
)

#Comunicados
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key = True)
    titulo = models.CharField(max_length=50, help_text="Ingrese el titulo del comunicado")
    detalle = models.TextField()
    detalle_corto = models.CharField(max_length=300)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, help_text="Eliga el departamento asociado")
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    tipo = TIPO_CHOICES

    def __str__(self):
        return self.titulo
