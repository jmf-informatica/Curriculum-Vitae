from django.contrib import admin
from django.urls import path
from .views import Education

urlpatterns = [
    path('', Education.as_view(),name='edu'),

]