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
    tablaLista_reproduccion = lista_reproduccion.objects.all().order_by('posicion')
    tablaRecomendaciones= recomendacion.objects.all()
    usuario = request.user

    return render(request, "listas.html", {'tablaVideos': tablaVideos, 'tablaCursos': tablaCursos, 'tablaLista_reproduccion': tablaLista_reproduccion, "user": usuario,'tablaRecomendaciones': tablaRecomendaciones})

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


@login_required(login_url='login')
def editar_listas(request, idCurso, nombreCurso):
    tablaCursos = cursos.objects.all()
    tablaVideos = videos.objects.all()
    tablaLista_reproduccion = lista_reproduccion.objects.all().order_by('posicion')
    tablaRecomendacion = recomendacion.objects.all()
    curso = idCurso
    nombre = nombreCurso

    listaEnCuestion = cursos.objects.get(id=curso)
    if listaEnCuestion.privacidad == False:
        Flag = False
    else:
        Flag = True



    if request.method == 'POST':
        identificador = request.POST.get('identificador')

        if identificador == "form3":
            IDeliminacion = request.POST.get('eliminar_id')
            eliminar = lista_reproduccion.objects.get(pk=IDeliminacion)
            eliminar.delete()
            return render(request, "editar_lista.html",{'tablaVideos': tablaVideos, 'tablaCursos': tablaCursos, 'tablaLista_reproduccion': tablaLista_reproduccion, "curso":curso, "nombre":nombre, "Flag": Flag, "tablaRecomendacion": tablaRecomendacion})
        
        if identificador == "form2":
            IDeliminacion = request.POST.get('eliminar_id_lista')
            eliminar = cursos.objects.get(pk=IDeliminacion)
            eliminar.delete()
            lista_reproduccion.objects.filter(id_curso=IDeliminacion).delete()
            return redirect('listas')
        if identificador == "form1":    
            NuevoNombre = request.POST.get('cambiar_nombre')
            if NuevoNombre:
                registro = cursos.objects.get(id = curso)
                registro.nombre_curso = NuevoNombre
                registro.save()
            return redirect('listas')
        if identificador == "form4":            
            pos1 = request.POST.get('pos1')
            pos2 = request.POST.get('pos2')
            
            vid1 = lista_reproduccion.objects.get(posicion = pos1)
            print(vid1)
            vid2 = lista_reproduccion.objects.get(posicion = pos2)
            print(vid2)
            vid1.posicion = pos2
            vid2.posicion = pos1
            vid1.save()
            vid2.save()

        elif identificador == "form5":
            listaCentral = curso
            listaSiguiente = request.POST.get('listaSiguiente', None)
            listaPrevia = request.POST.get('listaPrevia', None)
            evitar_repeticion =  recomendacion.objects.filter(lista_central=listaCentral).first()

            if evitar_repeticion:
                evitar_repeticion.lista_previa = listaPrevia
                evitar_repeticion.lista_siguiente = listaSiguiente
                evitar_repeticion.save()
            else:
                registro = recomendacion(lista_central= listaCentral, lista_previa = listaPrevia, lista_siguiente = listaSiguiente)
                registro.save()
            
    return render(request, "editar_lista.html",{'tablaVideos': tablaVideos, 'tablaCursos': tablaCursos, 'tablaLista_reproduccion': tablaLista_reproduccion, "curso":curso, "nombre":nombre, "Flag": Flag, "tablaRecomendacion": tablaRecomendacion})