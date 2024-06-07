from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flan,ContactForm
from .forms import ContactFormForm

# Create your views here.
def inicio(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html',{'datos':flanes_publicos} )

def acerca(request):
    return render(request, 'about.html')

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




#   flanes = Flan.objects.all()
#     