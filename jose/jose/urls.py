from django.urls import path
from jose_app import views

urlpatterns = [
    path('', views.listar_reservas, name='listar_reservas'),
    path('agregar/', views.agregar_reserva, name='agregar_reserva'),
    path('modificar/<int:pk>/', views.modificar_reserva, name='modificar_reserva'),
    path('eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
]