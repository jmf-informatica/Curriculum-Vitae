# Generated by Django 2.2.6 on 2020-02-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre carrera/curso')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace certificado')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Carrera/Curso',
                'verbose_name_plural': 'Carreras/Cursos',
                'ordering': ['nombre'],
            },
        ),
    ]
