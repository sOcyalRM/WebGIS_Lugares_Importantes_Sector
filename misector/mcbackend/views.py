from .models import Lugar, Ciudad, Categoria
from .serializers import SerializadorCategoria, SerializadorLugar
from rest_framework import generics

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