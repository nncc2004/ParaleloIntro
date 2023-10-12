# Generated by Django 4.2.5 on 2023-10-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0002_videos_clasificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso_usuario',
            name='UserCourseId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursos',
            name='CourseId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lista_reproduccion',
            name='ListId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='UserId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videos',
            name='VideoId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]