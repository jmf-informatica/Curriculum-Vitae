from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from webpersonal import settings

class ContactForm(forms.Form):
    name=forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba su nombre'}), min_length=3,max_length=50)
    phone=forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba su telefono de contacto'}), min_length=10,max_length=50)
    email=forms.EmailField(label='',required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Escriba su E-Mail'}),min_length=5,max_length=50)
    content=forms.CharField(label='',required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Deje su mensaje aquí','style':'max-height:300px;min-height:108px;'}),min_length=10,max_length=500)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
