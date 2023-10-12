from django.shortcuts import render

# Create your views here.
def prueba(request):
    
    return render(request, "prueba.html")

def principal(request):

    return render(request, "principal.html")

def nosotros(request):

    return render(request, "nosotros.html")