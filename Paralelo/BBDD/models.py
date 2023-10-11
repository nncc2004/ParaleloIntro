from django.db import models

# Create your models here.
class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    password = models.CharField(max_length=100)
    rol = models.BooleanField()

class curso_usuario(models.Model):
    id_curso = models.IntegerField()
    id_usuario = models.IntegerField()
    progreso = models.IntegerField()

class cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    cantidad_videos = models.IntegerField()
    autor = models.CharField(max_length=100)
    privacidad = models.BooleanField()

class lista_reproduccion(models.Model):
    id_curso = models.IntegerField()
    id_video = models.IntegerField()

class videos(models.Model):
    nombre_video = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    url = models.URLField()
    autor = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=100)