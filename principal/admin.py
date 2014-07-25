from django.contrib import admin

from principal.models import estudio,experiencia, funcionesTrabajo, grupoEstudio

class funcionesTrabajoInline( admin.StackedInline ):
    model = funcionesTrabajo  #modelo que se va utilizar
    extra = 1  #numero de registros en blanco que aparecen para llenar

class experienciaAdmin ( admin.ModelAdmin ):
    list_display = ( 'nombre_empresa', 'cargo', 'jefe', )
    search_fields = ( 'jefe', )    
    inlines = [funcionesTrabajoInline]
    
class funcionesTrabajoAdmin ( admin.ModelAdmin ):
    list_display = ( 'empresa', 'descripcion', )
    list_filter = ( 'empresa', )
    raw_id_fields = ( 'empresa', ) #me lo vuelve lupa por defecto queda en combo


class grupoEstudioAdmin ( admin.ModelAdmin ):
    filter_vertical = ( 'estudios', ) #permite agregar muchos registros de una manera muy facil de manera horizontal

admin.site.register( estudio )
admin.site.register( experiencia, experienciaAdmin )
admin.site.register( funcionesTrabajo, funcionesTrabajoAdmin )
admin.site.register( grupoEstudio, grupoEstudioAdmin )