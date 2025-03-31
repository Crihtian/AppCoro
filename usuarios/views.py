from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UsuarioAdminForm
from django.contrib.auth.models import User
from .models import Usuario

def is_admin(user):
    return user.is_staff

def login_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('usuarios:login')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('usuarios:lobby')
    return render(request, 'usuarios/login.html')

@login_required
def lobby_view(request):
    try:
        usuario = Usuario.objects.get(user=request.user)
        cuerda = usuario.get_cuerda_display()
    except Usuario.DoesNotExist:
        cuerda = "No asignada"
        
    return render(request, 'usuarios/lobby.html', {
        'es_director': request.user.groups.filter(name='director').exists(),
        'cuerda': cuerda
    })

@login_required
@user_passes_test(is_admin)
def crear_usuario(request):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para crear usuarios.')
        return redirect('usuarios:lobby')
        
    if request.method == 'POST':
        form = UsuarioAdminForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, f'Usuario creado exitosamente. Nombre de usuario: {usuario.user.username}, Contraseña provisional: CoroJovenGijon')
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioAdminForm()
    
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def lista_usuarios(request):
    usuarios = Usuario.objects.all().select_related('user').order_by('user__username')
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
@user_passes_test(is_admin)
def eliminar_usuario(request, usuario_id):
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para eliminar usuarios.')
        return redirect('usuarios:lobby')
        
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # No permitir eliminar al propio usuario
    if usuario.user == request.user:
        messages.error(request, 'No puedes eliminar tu propio usuario.')
        return redirect('usuarios:lista_usuarios')
    
    # Guardar el nombre del usuario para el mensaje
    nombre_usuario = usuario.user.get_full_name()
    
    # Eliminar primero el perfil y luego el usuario
    usuario.delete()
    usuario.user.delete()
    
    messages.success(request, f'Usuario {nombre_usuario} eliminado exitosamente.')
    return redirect('usuarios:lista_usuarios')
