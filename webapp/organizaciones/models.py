from django.db import models
from cuentas.models import User
from ckeditor.fields import RichTextField

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class OrgProfile(models.Model):
    

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='orgprofile')
   
    imagen = models.FileField(upload_to='o_perfiles', null=True, blank=True,verbose_name="Imagen",default='default.png')
    nombre=models.CharField(max_length=30,verbose_name="Nombre de la Organización")
    ruc = models.CharField(max_length=13, default='9999999999',null=True, blank=True,verbose_name="RUC")
    descripcion=models.TextField(max_length=800,verbose_name="Descripción")    
    website=models.URLField(max_length=300,null=True,blank=True,verbose_name="Página Web")
        
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)
    activo=models.BooleanField(default=False)
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    

    class Meta:
        
        verbose_name = 'Perfil de Organización'
        verbose_name_plural = 'Perfiles de Organizaciones'

    

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
        #print(instance.role)
    
    if kwargs.get('created', False) and instance.role=="organizacion":
        OrgProfile.objects.get_or_create(user=instance)