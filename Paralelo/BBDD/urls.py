from django.urls import path
from .views import principal, nosotros, registro, cursos, confirmacion
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', principal, name  = "principal"),
    path('nosotros/', nosotros, name = "nosotros"),
    path('registro/', registro, name = "registro"),
    path('login/', LoginView.as_view(template_name= "login.html"), name = "login"), 
    path('logout/', LogoutView.as_view(next_page= "principal"), name = "logout"),
    path('cursos/', cursos, name = "cursos"),
    path('confirmacion/', confirmacion, name = "confirmacion"),
]
