from django.contrib import admin
from .models import Educacion

# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display=('key','nombre','url','descripcion')

admin.site.register(Educacion,EducationAdmin)