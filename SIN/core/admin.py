from django.contrib import admin
from .models import Comunicado, Entidad

# Register your models here.
@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "logo")

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "entidad", "visible", "TIPO_CHOICES")

class SaveAndGet(admin.ModelAdmin):
    readonly_fields = ('publicado_por', 'modificado_por', 'entidad',)

    def save_model(self, request, obj, form, change):
        usuario = request.user
        if not obj.publicado_por:
            obj.publicado_por = usuario
        obj.modificado_por = usuario

        entidades = Entidad.objects.filter(admin=usuario).first()
        obj.entidad = entidades
        super(SaveAndGet, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        query = super(SaveAndGet, self).get_queryset(request)
        if not request.user.is_superuser:
            query = query.filter(publicado_por = request.user)
        return query
