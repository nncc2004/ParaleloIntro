from django.urls import path
from .views import principal, nosotros, registro, view_cursos, confirmacion, listas, crear_listas, crear_listas_publicas
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', principal, name  = "principal"),
    path('nosotros/', nosotros, name = "nosotros"),
    path('registro/', registro, name = "registro"),
    path('login/', LoginView.as_view(template_name= "login.html"), name = "login"), 
    path('logout/', LogoutView.as_view(next_page= "principal"), name = "logout"),
    path('cursos/', view_cursos, name = "cursos"),
    path('confirmacion/', confirmacion, name = "confirmacion"),
    path('listas/', listas, name = "listas"),
    path('crear_listas/', crear_listas, name = "crear_listas"),
    path('crear_listas_publicas/', crear_listas_publicas, name = "crear_listas_publicas"),
]
