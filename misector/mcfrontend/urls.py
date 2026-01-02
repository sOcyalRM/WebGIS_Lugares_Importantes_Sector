from django.urls import path
from . import views

app_name = 'mcfrontend'

urlpatterns = [
    path ('', views.listaLugaresMap, name='ListaLugaresMap'),
]