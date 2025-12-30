from django.urls import path
from .import views

urlpatterns = [
    path('categorias/', views.ListaCategoria.as_view(), name = views.ListaCategoria.name),
    path('categorias/<int:pk>/', views.DetalleCategoria.as_view(), name = views.DetalleCategoria.name),
    path('lugares/', views.ListaLugar.as_view(), name = views.ListaLugar.name),
    path('lugares/<int:pk>/', views.DetalleLugar.as_view(), name = views.DetalleLugar.name),

]