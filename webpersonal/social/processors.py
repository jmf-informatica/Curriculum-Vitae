from .models import Link

def ctx_social(request):
    ''' Esta función crea un diccionario con todos las url del modelo link y los retorna como contexto para la impresion en plantilla '''
    ctx={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    
    return ctx