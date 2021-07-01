from django.db import models
from django.core.validators import FileExtensionValidator
from cuentas.models import User
from organizaciones.models import OrgProfile
from django.urls import reverse
from cuentas.models import User
from django.core.exceptions import ValidationError


class Jobs(models.Model):
    TIPO_CHOICES = [
        ('parcial', 'TIEMPO PARCIAL'),
        ('completo', 'TIEMPO COMPLETO'),
        ('remoto', 'REMOTO'),
    ]
    TIPO_CATEGORIA = [
        ('pasantia', 'PASANTIA'),
        ('empleo', 'EMPLEO'),
        ('voluntariado', 'VOLUNTARIADO'),
        ('otro','OTRO')
    ]
    TIPO_ZONAS = [
        ('costa', 'COSTA'),
        ('sierra', 'SIERRA'),
        ('oriente', 'ORIENTE'),
        ('galapagos', 'GALAPAGOS'),

    ]
    organizacion=models.ForeignKey(OrgProfile,on_delete=models.CASCADE,related_name="org_profiles")
    titulo=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30, choices=TIPO_CHOICES, default='empleo')
    categoria=models.CharField(max_length=30, choices=TIPO_CATEGORIA, default='completo')
    zona=models.CharField(max_length=30, choices=TIPO_ZONAS, default='sierra')
    ciudad=models.CharField(max_length=30)
    salario=models.CharField(max_length=30)
    descripcion=models.TextField(max_length=800)
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    fecha_cierre=models.DateField()
    activo=models.BooleanField(default=False)
    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('job-list', kwargs={'pk': self.pk}) 
    class Meta:
        ordering = ["-fecha_publicacion"]

def user_directory_path_cv(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    return 'user_{0}/{1}'.format("cv_"+str(instance.applicant.id), filename)
    
def user_directory_path_cp(instance, filename):
    print(instance)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format("cp_"+str(instance.applicant.id), filename)
""""
def validate_file(archivo):
    file_size =archivo.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024*1024:
        raise ValidationError("Máximo tamaño permitido es %s Mb" % limit_mb)
"""

class Applicants(models.Model):
    job = models.ForeignKey(
        Jobs, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(upload_to=user_directory_path_cv,default='default.png',validators=[FileExtensionValidator
(allowed_extensions=['pdf', 'docx'])])
    cp = models.FileField(upload_to=user_directory_path_cp,default='default.png',validators=[FileExtensionValidator
(allowed_extensions=['pdf', 'docx'])]) 
    fecha_aplicacion=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.applicant.email

    def get_absolute_url(self):
        return reverse('empleos:detail-job', kwargs={'pk': self.pk})
""""
    def get_path_cv(self):
        if self.cv.path:
            return self.cv.path

    def get_path_cp(self):
        if self.cp.path:
            return self.cp.path
"""

class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Jobs, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='applied_user', on_delete=models.CASCADE)
      
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.titulo

class SavedJobs(models.Model):
    job = models.ForeignKey(
    Jobs, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.titulo

class Selected(models.Model):
    job = models.ForeignKey(
        Jobs, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant.email
# Create your models here.
