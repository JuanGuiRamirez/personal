from django.contrib import admin

from principal.models import estudio,experiencia, funcionesTrabajo


class experienciaAdmin ( admin.ModelAdmin ):
    list_display = ( 'nombre_empresa', 'cargo', 'jefe', )
    search_fields = ( 'jefe', )
    
class funcionesTrabajoAdmin ( admin.ModelAdmin ):
    list_display = ( 'empresa', 'descripcion', )
    list_filter = ( 'empresa', )

admin.site.register( estudio )
admin.site.register( experiencia, experienciaAdmin )
admin.site.register( funcionesTrabajo, funcionesTrabajoAdmin )
