from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Lugar

# Create your views here.

def todos_lugares(request):
    queryset = Lugar.objects.all()
    geojason = serialize('geojson', queryset, geometry_field = 'polygon_geom', srid = 3857)
    return HttpResponse(geojason, content_type = 'application/json')

def detalle_lugar(request, pk):
    data = []

    try:
        lugar = Lugar.objects.get(pk = pk)
        data.append(lugar)
    except Lugar.DoesNotExist:
        pass

    geojson = serialize('geojson', data, geometry_field = 'polygon_geom', srid = 3857)
    return HttpResponse(geojson, content_type= 'application/json')
