from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField('Nombre de Categoria', max_length = 50, 
                                       help_text = 'Especifica la categoria del lugar')
    creado_en = models.DateTimeField(auto_now_add = True)
    modificado_en = models.DateTimeField(auto_now = True)

    class Meta: 
        verbose_name_plural = 'Categorias'

    def __str__ (self):
        return self.nombre_categoria
    
class Lugar(models.Model):
    categorias = models.ForeignKey('Categoria', on_delete = models.CASCADE) #CASCADE provoca un efecto en cascada/cadena cuando se elimina un record
    nombre_lugar = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 254, blank = True)
    creado_en = models.DateTimeField(auto_now_add = True)
    modificado_en = models.DateTimeField(auto_now = True)
    campo_imagen = models.ImageField(upload_to='imagen_lugar', blank=True, null=True)
    activo = models.BooleanField(default = True)
    place_geom = models.PolygonField()

    class Meta:
        verbose_name_plural = 'Lugares'

    def __str__(self):
        return self.nombre_lugar

class Ciudad (models.Model):
    nombre_ciudad = models.CharField(max_length = 50)
    punt_geom = models.PointField(null=True)

    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.nombre_ciudad
    