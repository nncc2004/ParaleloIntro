# Generated by Django 4.2.5 on 2023-10-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0003_curso_usuario_usercourseid_cursos_courseid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso_usuario',
            name='UserCourseId',
            field=models.IntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='CourseId',
            field=models.IntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lista_reproduccion',
            name='ListId',
            field=models.IntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='UserId',
            field=models.IntegerField(verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='VideoId',
            field=models.IntegerField(verbose_name='ID'),
        ),
    ]
