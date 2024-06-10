from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('acerca/', views.acerca),
    path('bienvenido/', views.bienvenido),
    path('contacto/', views.contacto,name='contacto'),
    path('exito/', views.exito),
    path('logout/', views.cerrar_sesion, name ='logout'),
    path('login/',views.iniciar_sesion,name='login'),
    path('Flan/agregar/', views.crear_flan,name='agregarFlan'),
    path('flan/editar/',views.editar_flan,name='editarFlan')
]
