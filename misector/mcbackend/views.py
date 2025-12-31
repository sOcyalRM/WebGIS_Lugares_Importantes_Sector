from .models import Lugar, Ciudad, Categoria
from .serializers import SerializadorCategoria, SerializadorLugar, SerializadorCiudad
from rest_framework import generics

from django.http import Http404
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

# Create your views here.
class ListaCategoria (generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = SerializadorCategoria
    name = 'lista-categoria'

class DetalleCategoria (generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = SerializadorCategoria
    name = 'detalle-categoria'

class ListaLugar(generics.ListAPIView):
    queryset = Lugar.objects.filter(activo = True)
    serializer_class = SerializadorLugar
    name = 'lista-lugares'

class DetalleLugar(generics.RetrieveAPIView):
    queryset = Lugar.objects.filter(activo = True)
    serializer_class = SerializadorLugar
    name = 'detalle-lugares'

class ListaCiudad (generics.ListAPIView):
    serializer_class = SerializadorCiudad
    name = 'lista-ciudad'

    def get_queryset(self):
        lugarID = self.request.query_params.get('lugarID')

        if lugarID is None:
            raise Http404
        
        selectedPlaceGeom = get_object_or_404(Lugar, pk = lugarID).place_geom
        nearestCities = Ciudad.objects.annotate(distancia = Distance('punt_geom', selectedPlaceGeom)).order_by('distancia')[:3]
        return nearestCities
