from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegistroDeusuario(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label='Ingresa una contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma la contraseña', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class CrearListaForm(forms.ModelForm):
    nombre_curso = forms.CharField(label="Nombre lista")
    class Meta:
        model = cursos
        fields = ['nombre_curso']