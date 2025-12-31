from .models import Lugar, Categoria, Ciudad
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class SerializadorCategoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SerializadorLugar(GeoFeatureModelSerializer):
    categorias = serializers.SlugRelatedField(queryset = Categoria.objects.all(), slug_field='nombre_categoria')

    class Meta:
        model = Lugar
        geo_field = 'place_geom'

        fields = (
            'pk',
            'categorias',
            'nombre_lugar',
            'descripcion',
            'creado_en',
            'modificado_en',
            'campo_imagen'
        )
class SerializadorCiudad (GeoFeatureModelSerializer):
    proximity = serializers.SerializerMethodField('get_proximidad')

    def get_proximidad(self, obj):
        if obj.distancia:
            return obj.distancia.km
        return False
    
    class Meta:
        model = Ciudad
        geo_field = 'punt_geom'

        fields = (
            'pk',
            'nombre_ciudad',
            'proximity'
        )