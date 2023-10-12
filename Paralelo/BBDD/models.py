from django.db import models

# Create your models here.
class curso_usuario(models.Model):
    UserCourseId = models.IntegerField(verbose_name= "ID")
    id_curso = models.IntegerField()
    id_usuario = models.IntegerField()
    progreso = models.IntegerField()
    def __str__(self):
        return "ID: %s. IdCurso: %s. IdUsuario: %s. Progreso: %s." %(self.UserCourseId, self.id_curso, self.id_usuario, self.progreso)

class cursos(models.Model):
    CourseId = models.IntegerField(verbose_name= "ID")
    nombre_curso = models.CharField(max_length=100)
    cantidad_videos = models.IntegerField()
    autor = models.CharField(max_length=100)
    privacidad = models.BooleanField()
    def __str__(self):
        return "ID: %s. Nombre_Curso: %s. Cantidad_Videos: %s. Autor: %s. Privacidad: %s." %(self.CourseId, self.nombre_curso, self.cantidad_videos, self.autor, self.privacidad)

class lista_reproduccion(models.Model):
    ListId = models.IntegerField(verbose_name= "ID")
    id_curso = models.IntegerField()
    id_video = models.IntegerField()
    def __str__(self):
        return "ID: %s. IdCurso: %s. IdVideo: %s." %(self.ListId, self.id_curso, self.id_video)
class videos(models.Model):
    VideoId = models.IntegerField(verbose_name= "ID")
    nombre_video = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    url = models.URLField()
    autor = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=100)
    def __str__(self):
        return "ID: %s. Nombre_video: %s. Duración: %s. URL: %s. Autor: %s, Clasificación: %s" %(self.VideoId, self.nombre_video, self.duracion, self.url, self.autor, self.clasificacion)