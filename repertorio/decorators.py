from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .models import Director

def director_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Debes iniciar sesión primero.')
            return redirect('login')
        try:
            director = Director.objects.get(usuario=request.user)
            return view_func(request, *args, **kwargs)
        except Director.DoesNotExist:
            messages.error(request, 'No tienes permisos de director para realizar esta acción.')
            return redirect('repertorio:lista')
    return _wrapped_view 