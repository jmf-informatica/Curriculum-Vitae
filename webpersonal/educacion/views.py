from django.shortcuts import render
from .models import Educacion
from django.views.generic import TemplateView

# Create your views here.

class Education(TemplateView):
    template_name='educacion/educacion.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['analista'] = Educacion.objects.filter(nombre='Analista de Sistemas de Computación')
        context['ccna'] = Educacion.objects.filter(nombre='CCNA')
        context['comptia'] = Educacion.objects.filter(nombre='COMPTIA A+ ESSENTIALS')
        return context