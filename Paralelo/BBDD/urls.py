from django.urls import path
from .views import principal, registro, view_cursos, confirmacion, listas, crear_listas, crear_listas_publicas, crear_recomendiacion, editar_listas
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', principal, name  = "principal"),
    path('registro/', registro, name = "registro"),
    path('login/', LoginView.as_view(template_name= "login.html"), name = "login"), 
    path('logout/', LogoutView.as_view(next_page= "principal"), name = "logout"),
    path('cursos/', view_cursos, name = "cursos"),
    path('confirmacion/', confirmacion, name = "confirmacion"),
    path('listas/', listas, name = "listas"),
    path('crear-listas/', crear_listas, name = "crear_listas"),
    path('crear-listas_publicas/', crear_listas_publicas, name = "crear_listas_publicas"),
    path('crear-recomendacion/', crear_recomendiacion, name = "crear_recomendacion"),
    path('editar-lista/<int:idCurso>/<nombreCurso>', editar_listas, name = "editar_lista"),
    #recuperacion de contraseñas
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name= 'resetPassword.html'), name="password_reset"),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'CorreoEnviado.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('accounts/login/', LoginView.as_view(template_name= "login.html")), 

]
#template_name="newPassword.html"