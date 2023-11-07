from django.db import models

# Create your models here.
class cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    cantidad_videos = models.IntegerField(default=0)
    autor = models.IntegerField()
    privacidad = models.BooleanField(default=True)
    def __str__(self):
        return "Nombre_Curso: %s. Cantidad_Videos: %s. Autor: %s. Privacidad: %s." %( self.nombre_curso, self.cantidad_videos, self.autor, self.privacidad)

class lista_reproduccion(models.Model):
    id_curso = models.IntegerField()
    id_video = models.IntegerField()
    posicion = models.IntegerField(null=True)
    def save(self, *args, **kwargs):
        if not self.posicion:

            max_posicion = lista_reproduccion.objects.aggregate(models.Max('posicion'))['posicion__max']
            if max_posicion is not None:
                self.posicion = max_posicion + 1
            else:
                self.posicion = 1
        super(lista_reproduccion, self).save(*args, **kwargs)
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
    
class recomendacion(models.Model):
    lista_central = models.IntegerField(default=-1)
    lista_previa = models.IntegerField(default=-1)
    lista_siguiente = models.IntegerField(default=-1)

    def __str__(self):
        return "Lista central: %s. Lista previa: %s. Lista siguiente: %s" %(self.lista_central, self.lista_previa, self.lista_siguiente)
