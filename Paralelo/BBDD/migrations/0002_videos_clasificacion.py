# Generated by Django 4.2.5 on 2023-10-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='clasificacion',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
