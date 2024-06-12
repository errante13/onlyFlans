from django.db import models
import uuid
# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField( max_length=64)
    description= models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    
    #atributos adicionales de fecha
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default = uuid.uuid4,editable = False) 
    customer_email = models.EmailField()
    customer_name = models.CharField( max_length=64)
    message = models.TextField()
    
     #atributos adicionales de fecha
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.customer_email 