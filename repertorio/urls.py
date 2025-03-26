from django.urls import path
from . import views

app_name = 'repertorio'

urlpatterns = [
    path('', views.lista_canciones, name='lista'),
    path('agregar/', views.agregar_cancion, name='agregar'),
] 