# Generated by Django 4.2.5 on 2023-10-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0008_videos_tematica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='privacidad',
            field=models.IntegerField(),
        ),
    ]
