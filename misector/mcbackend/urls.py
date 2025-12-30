from django.urls import path
from .import views

urlpatterns = [
    path('lugares/', views.todos_lugares, name = 'TodosLugares'),
    path('lugares/<int:pk>/', views.detalle_lugar, name = 'detalle_lugar'),
]