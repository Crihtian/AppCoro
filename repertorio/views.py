from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cancion
from .forms import CancionForm
from .decorators import director_required

# Create your views here.

@login_required
def lista_canciones(request):
    canciones = Cancion.objects.all().order_by('repertorio', 'nombre')
    repertorios = dict(Cancion.REERTORIO_CHOICES)
    return render(request, 'repertorio/lista_canciones.html', {
        'canciones': canciones,
        'repertorios': repertorios,
        'es_director': hasattr(request.user, 'director')
    })

@director_required
def agregar_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST, request.FILES)
        if form.is_valid():
            cancion = form.save(commit=False)
            cancion.creado_por = request.user
            cancion.save()
            messages.success(request, 'Canción agregada exitosamente.')
            return redirect('repertorio:lista')
    else:
        form = CancionForm()
    
    return render(request, 'repertorio/agregar_cancion.html', {
        'form': form
    })
