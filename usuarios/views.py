from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm

def registro_usuario(request):
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('inicio')
    return render(request, 'usuarios/registro.html', {'form': form})

def inicio_sesion(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('inicio')
    return render(request, 'usuarios/login.html', {'form': form})

def ver_perfil(request):
    return render(request, 'usuarios/perfil.html')

def logout_usuario(request):
    logout(request)
    return redirect('inicio')
