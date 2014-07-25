from django.db import models
from test.test_imageop import MAX_LEN

class experiencia ( models.Model ):
    nombre_empresa = models.CharField( max_length = 120 )
    cargo = models.CharField( max_length = 120 )
    jefe = models.CharField( max_length = 120 )
    celular = models.CharField( max_length=20 )
    telefono = models.CharField( max_length = 20 )
    
    def __str__(self):
        return self.nombre_empresa
    

class funcionesTrabajo ( models.Model ):
    empresa = models.ForeignKey( experiencia )
    descripcion = models.CharField( max_length=150 )
    
    def __str__(self):
        return self.descripcion
    
    
class estudio ( models.Model ):
    titulo = models.CharField( max_length = 120 )
    institucion = models.CharField( max_length = 120 )
    diploma = models.ImageField(upload_to = 'images_diploma')
    descripcion = models.CharField( max_length = 255 )
    
    def __str__(self):
        return self.titulo
    
class grupoEstudio ( models.Model ):
    descripcion = models.CharField( max_length = 140 )
    estudios = models.ManyToManyField ( estudio )