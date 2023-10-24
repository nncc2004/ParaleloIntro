from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import RegistroDeusuario, CrearListaForm
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
def view_cursos(request):
    usuario = request.user
    tablaCursos = cursos.objects.all()
    tablaVideos = videos.objects.all()
    
    temas = []
    cursosCoincidentes = []
    for x in tablaVideos:
        a = str(x.tematica)
        if a not in temas:
            temas.append(a)
    for x in tablaCursos:
            if x.autor == usuario.id:
                cursosCoincidentes.append(x)

    if request.method == 'POST':
        infoValue = request.POST.get('listas', None)
        infoValue = infoValue.split(",")
        IdCursoSeleccionado = int(infoValue[0])
        IdVideoSeleccionado = int(infoValue[1])

        if infoValue:
            registroCurso = lista_reproduccion(id_curso=IdCursoSeleccionado, id_video=IdVideoSeleccionado)
            registroCurso.save()
            return redirect('cursos')

    return render(request, "Cursos.html", {'tablaVideos': tablaVideos, 'tematicas': temas, "cursosCoincidentes": cursosCoincidentes})


@login_required(login_url='login')
def listas(request):
    tablaCursos = cursos.objects.all()
    tablaVideos = videos.objects.all()
    tablaLista_reproduccion = lista_reproduccion.objects.all()
    usuario = request.user
    
    if request.method == 'POST':
        if 'eliminar_id' in request.POST:
            IDeliminacion = request.POST.get('eliminar_id')
            eliminar = lista_reproduccion.objects.get(pk=IDeliminacion)
            eliminar.delete()
            return render(request, "listas.html", {'tablaVideos': tablaVideos, 'tablaCursos': tablaCursos, 'tablaLista_reproduccion': tablaLista_reproduccion, "user": usuario})
        
        if 'eliminar_id_lista' in request.POST:
            IDeliminacion = request.POST.get('eliminar_id_lista')
            eliminar = cursos.objects.get(pk=IDeliminacion)
            eliminar.delete()
            lista_reproduccion.objects.filter(id_curso=IDeliminacion).delete()
            return render(request, "listas.html", {'tablaVideos': tablaVideos, 'tablaCursos': tablaCursos, 'tablaLista_reproduccion': tablaLista_reproduccion, "user": usuario})
    

    return render(request, "listas.html", {'tablaVideos': tablaVideos, 'tablaCursos': tablaCursos, 'tablaLista_reproduccion': tablaLista_reproduccion, "user": usuario})

@login_required(login_url='login')
def crear_listas(request):
    if request.method == 'POST':
        form = CrearListaForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            autor = request.user
            idUser = autor.id
            curso.autor = idUser
            curso.save()
        return redirect('listas')
    else:
        form = CrearListaForm()
    
    return render(request, "crear_listas.html", {'form': form})

@login_required(login_url='login')
def crear_listas_publicas(request):
    if request.method == 'POST':
        form = CrearListaForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            autor = request.user
            idUser = autor.id
            curso.autor = idUser
            curso.privacidad = False
            curso.save()
        return redirect('listas')
    else:
        form = CrearListaForm()
    
    return render(request, "crear_listas_publicas.html", {'form': form})