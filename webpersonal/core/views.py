from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name='core/index.html'

class About(TemplateView):
    template_name='core/about-me.html'
    

class Skills(TemplateView):
    template_name='core/skills.html'


class Experiencias(TemplateView):
    template_name='core/experiencias.html'

def mi_error_404(request, exception):
    return render(request,'core/error_404.html')