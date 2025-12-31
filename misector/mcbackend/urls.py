from django.urls import path
from .import views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('categorias/', views.ListaCategoria.as_view(), name = views.ListaCategoria.name),
    path('categorias/<int:pk>/', views.DetalleCategoria.as_view(), name = views.DetalleCategoria.name),
    path('lugares/', views.ListaLugar.as_view(), name = views.ListaLugar.name),
    path('lugares/<int:pk>/', views.DetalleLugar.as_view(), name = views.DetalleLugar.name),
    path('ciudades/',views.ListaCiudad.as_view(), name = views.ListaCiudad.name),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)