from django.urls import path
from .views import principal, nosotros, prueba
urlpatterns = [
    path('', principal, name  = "principal"),
    path('nosotros/', nosotros, name = "nosotros"),
    path('prueba/', prueba, name = "prueba"),
]
