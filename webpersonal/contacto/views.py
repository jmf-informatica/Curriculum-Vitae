from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from contacto.decorators import check_recaptcha

# Create your views here.


@check_recaptcha
def contacto(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(data=request.POST)
        if ContactForm.is_valid:
            name=request.POST.get('name','')
            phone=request.POST.get('phone','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #Enviando correo y redireccionando
            email=EmailMessage(
                'Curriculum-JMF: Nuevo mensaje de contacto', # Asunto del mensaje
                '\n De: {}\n Telefono: {}\n Email: {}\n Mensaje: {}'.format(name,phone,email,content), # Cuerpo del mensaje
                'no-reply@jmfittipaldi.com.ar', # Email de origen
                ['contacto@jmfittipaldi.com.ar','jmfittipaldi@gmail.com'], # Email destino
                reply_to=[email] # Responder a:
            )
            try:
                email.send()
                return redirect(reverse('contacto:contacto')+"?ok")
            except:
                return redirect(reverse('contacto:contacto')+"?fail")
            
    return render(request,'contacto/contacto.html',{'form':form})