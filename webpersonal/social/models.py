from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name='Clave', max_length=100,unique=True)
    name = models.CharField(verbose_name='Red Social', max_length=100)
    url = models.URLField(verbose_name='Enlace', max_length=100, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name