from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('acerca/', views.acerca),
    path('bienvenido/', views.bienvenido),
    path('contacto/', views.contacto,name='contacto'),
    path('exito/', views.exito)
    
]
