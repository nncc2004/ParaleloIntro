# Generated by Django 4.2.5 on 2023-10-14 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0010_alter_cursos_privacidad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='curso_usuario',
        ),
    ]
