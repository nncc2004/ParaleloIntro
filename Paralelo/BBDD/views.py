from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import RegistroDeusuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroDeusuario(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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

def confirmacion(request):
    
    return render(request, 'confirmacion.html')

@login_required(login_url='login')
def cursos(request):
    tablaVideos = videos.objects.all()
    temas = []
    for x in tablaVideos:
        a = str(x.tematica)
        if a not in temas:
            temas.append(a)

    return render(request, "Cursos.html", {'tablaVideos': tablaVideos, 'tematicas': temas})