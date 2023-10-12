from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import RegistroDeusuario
from django.contrib.auth.models import User

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroDeusuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Usuario {username} ha sido creado exitosamente")
            return redirect('principal')
    else:
        form = RegistroDeusuario()
    context = {'form' : form}

    return render(request, "registro.html", context)

def principal(request):
    usuario = request.user
    return render(request, "principal.html", {'usuario': usuario})

def nosotros(request):

    return render(request, "nosotros.html")