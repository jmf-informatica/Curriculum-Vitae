from django.db import models

# Create your models here.

class Educacion(models.Model):
    key = models.SlugField(verbose_name='Clave', max_length=100,unique=True)
    nombre = models.CharField(verbose_name='Nombre carrera/curso',max_length=100)
    url = models.URLField(verbose_name='Enlace certificado',max_length=200,blank=True,null=True)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=500)

    class Meta:
        verbose_name='Carrera/Curso'
        verbose_name_plural='Carreras/Cursos'
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre