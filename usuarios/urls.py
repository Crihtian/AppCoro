from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('lobby/', views.lobby_view, name='lobby'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
] 