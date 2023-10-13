from django.db import models

# Create your models here.
class curso_usuario(models.Model):
    id_curso = models.IntegerField()
    id_usuario = models.IntegerField()
    progreso = models.IntegerField()
    def __str__(self):
        return "IdCurso: %s. IdUsuario: %s. Progreso: %s." %(self.id_curso, self.id_usuario, self.progreso)

class cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    cantidad_videos = models.IntegerField()
    autor = models.CharField(max_length=100)
    privacidad = models.BooleanField()
    def __str__(self):
        return "Nombre_Curso: %s. Cantidad_Videos: %s. Autor: %s. Privacidad: %s." %( self.nombre_curso, self.cantidad_videos, self.autor, self.privacidad)

class lista_reproduccion(models.Model):
    id_curso = models.IntegerField()
    id_video = models.IntegerField()
    def __str__(self):
        return "IdCurso: %s. IdVideo: %s." %(self.id_curso, self.id_video)
    
class clasificacion(models.Model):
    tema = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.tema
    def save(self, *args, **kwargs):
        self.tema = self.tema.upper()
        existing_clasificacion = clasificacion.objects.filter(tema=self.tema)
        
        if existing_clasificacion.exists():
            return
        super().save(*args, **kwargs)
    
class videos(models.Model):
    nombre_video = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    url = models.URLField()
    autor = models.CharField(max_length=100)
    tematica = models.ForeignKey(clasificacion, on_delete = models.PROTECT, to_field="tema")
    def __str__(self):
        return "Nombre_video: %s. Duración: %s. URL: %s. Autor: %s, Tema: %s" %(self.nombre_video, self.duracion, self.url, self.autor, self.tematica)
