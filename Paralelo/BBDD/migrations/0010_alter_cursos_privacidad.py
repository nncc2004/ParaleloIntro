# Generated by Django 4.2.5 on 2023-10-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0009_alter_cursos_privacidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='privacidad',
            field=models.BooleanField(default=False),
        ),
    ]
