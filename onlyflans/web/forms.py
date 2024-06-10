from django import forms

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label = 'correo')
    customer_name = forms.CharField(max_length=64,label ='nombre')
    message = forms.CharField(label = 'Mensaje')
    
class FlanForm(forms.Form):
    flan_uuid = forms.UUIDField(label = 'uuid')
    name = forms.CharField( max_length=64,label='nombre')
    description= forms.CharField(label = 'Mensaje')
    image_url = forms.URLField(label = 'imagen')
    slug = forms.SlugField(label = 'slug')
    is_private = forms.BooleanField(label = 'privado',required=False)
    