from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
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
    return render(request, 'usuarios/lobby.html')
