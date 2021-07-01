from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from cuentas.managers import CustomUserManager
from django.db.models.signals import post_save
#from empleos.models import Jobs

ROLE = (
    ('organizacion', "Organizacion"),
    ('persona', "Persona"),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "Ya existe un usuario registrado con ese correo.",
                              })
    first_name=models.CharField(max_length=30,verbose_name="Nombre")
    last_name=models.CharField(max_length=30,verbose_name="Apellido")
    role = models.CharField(choices=ROLE,  max_length=20)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()

class Ods(models.Model):
    ODS_CHOICES = [
        ('Fin Pobreza', 'Fin Pobreza'),
        ('Hambre Cero', 'Hambre Cero'),
        ('Salud y Bienestar', 'Salud y Bienestar'),
        ('Educación de Calidad', 'Educación de Calidad'),
        ('Igualdad de Género', 'Igualdad de Género'),
        ('Agua Limpia y Saneamiento', 'Agua Limpia y Saneamiento'),
        ('Energía Asequible y Limpia', 'Energía Asequible y Limpia'),
        ('Trabajo decente y Crecimeinto Económico', 'Trabajo decente y Crecimeinto Económico'),
        ('Industrial Innovación e Infraestructuras', 'Industrial Innovación e Infraestructuras'),
        ('Reducción de Desigualdades', 'Reducción de Desigualdades'),
        ('Ciudades y Comunidades Sostenibles', 'Ciudades y Comunidades Sostenibles'),
        ('Producción y Consumos Resposables', 'Producción y Consumos Resposables'),
        ('Acción por el Clima', 'Acción por el Clima'),
        ('Vida Submarina', 'Vida Submarina'),
        ('Vida de Ecositemas Terrestres', 'Vida de Ecositemas Terrestres'),
        ('Paz Justicia e Instituciones Sólidas', 'Paz Justicia e Instituciones Sólidas'),
        ('Alianza para lograr los objetivos', 'Alianza para lograr los objetivos'),
       
    ]
    intereses=models.CharField(choices=ODS_CHOICES,max_length=100, default='Fin Pobreza')
    def __str__(self):
        return self.intereses

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='userprofile')
    descripcion=models.TextField(max_length=500,null=True,blank=True,verbose_name='Sobre mi')
    imagen = models.FileField(upload_to='u_perfiles', null=True, blank=True,default='default.png')
    ods=models.ManyToManyField(Ods)
    cedula = models.CharField(max_length=10, default='9999999999',null=True, blank=True,verbose_name="Cédula")    
    direccion=models.CharField(max_length=100,verbose_name="Dirección")
    telefono=models.CharField(max_length=10,verbose_name="Teléfono")
    activo=models.BooleanField(default=True)
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now=True)

    

    class Meta:
        
        verbose_name = 'Perfil de personas'
        verbose_name_plural = 'Pefiles de personas'
  
class Ods_profile(models.Model):
    ods = models.ForeignKey(Ods, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    
    if kwargs.get('created', False) and instance.role=="persona":
        Profile.objects.get_or_create(user=instance)
        

