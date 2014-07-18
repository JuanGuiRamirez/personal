from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

juan guillermo

#import para vistas genericas
from django.views.generic import list_detail
from principal.models import experiencia, funcionesTrabajo

def get_exp():
    return funcionesTrabajo.objects.all( )

list_experiencia = {
                    "queryset" : experiencia.objects.all(),     #consulta para la vista generica
                    #cambia el nombre de la variable que va pasar los datos por defecto es object_list como se ve en la url
                    # yo lo puedo cambiar por otro y en la plantilla le debo agregar al final del nombre '_list'
                    "template_object_name" : "exp_anterior" ,    
                    #puedo pasar un contexto extra 
                    "extra_context" : { "funciones" : funcionesTrabajo.objects.all }, 
                    #para decir el nombre de la plantilla de lo contrario el toma un nombre por defecto
                    #tenendo en cuenta la app/modelo_list.html
                    "template_name" : "nombre.html",
                    }



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.index'),
    url(r'^experiencia/', list_detail.object_list, list_experiencia),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
