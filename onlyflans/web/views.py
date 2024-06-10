from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from .models import Flan,ContactForm
from .forms import ContactFormForm,FlanForm
# Create your views here.
def inicio(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'datos':flanes_publicos} )

def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenido(request):
    
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'datos':flanes_privados})


def exito(request):
    return render(request, 'exito.html')


def contacto(request):
    #validar metodo post
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        #validar información correcta
        if form.is_valid():
            #guardado de la información en la base de datos
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            
            # redirección del metodo
            return HttpResponseRedirect('/exito')

    else: 
        # redirección del metodo
        form = ContactFormForm()
            
    return render(request,'contacto.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request,"sesión cerrada con éxito")
    return redirect('/')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request,'registration/login.html')   
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {"error": "Usuario o password es incorrecto."})
        else:
            login(request, user)
            return redirect('/bienvenido')

@login_required         
def crear_flan(request):
    #validar metodo post
    if request.method == 'POST':
        form = FlanForm(request.POST)
        #print(request.POST)
        #validar información correcta
        if form.is_valid():
            #guardado de la información en la base de datos
            guardar_Flan = Flan.objects.create(**form.cleaned_data)
            # redirección del metodo
            messages.success(request,'Flan Agregado con Éxito')
            return redirect('/bienvenido')
    else: 
        # redirección del metodo
        form = FlanForm()
    return render(request,'crear_flan.html', {'form':form})


@login_required
def editar_flan(request):
    messages.error(request,'función en desarrollo, disculpes las molestias')
    return redirect('agregarFlan')

