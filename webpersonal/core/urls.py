from django.contrib import admin
from django.urls import path
from .views import Home, About, Skills, Experiencias

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('sobre-mi/', About.as_view(),name='about'),
    path('skills/', Skills.as_view(),name='skills'),
    path('experiencias/', Experiencias.as_view(),name='experiencias'),
]