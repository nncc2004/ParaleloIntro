from django.contrib import admin
from BBDD.models import lista_reproduccion, cursos, videos, clasificacion
# Register your models here.


class CursosAdmin(admin.ModelAdmin):
    list_display = ( "nombre_curso", "cantidad_videos", "autor", "privacidad")
    search_fields = ( "nombre_curso", "cantidad_videos", "autor", "privacidad")
    list_filter = ("privacidad",)


class listaAdmin(admin.ModelAdmin):
    list_display = ("id_curso", "id_video")
    search_fields = ( "id_curso", "id_video")

class VideoAdmin(admin.ModelAdmin):
    list_display = ( "nombre_video", "duracion", "url", "autor", "tematica")
    search_fields = ( "nombre_video", "duracion", "url", "autor", "tematica__tema")
    list_filter = ("autor", "tematica__tema", )



admin.site.register(cursos, CursosAdmin)
admin.site.register(lista_reproduccion,listaAdmin)
admin.site.register(videos, VideoAdmin)
admin.site.register(clasificacion)
