
from django.contrib import admin
from .models import Applicants, AppliedJobs, Jobs, SavedJobs, Selected
from organizaciones.models import OrgProfile  
# Register your models here.

class JobsAdmin(admin.ModelAdmin):

    def get_nombre(self, obj):
        return obj.organizacion.nombre
    

    class Meta:
        model = Jobs
        fields = ('organizacion','titulo','descripcion')
    list_display=('get_nombre','titulo','descripcion')
    readonly_fields=('fecha_publicacion',)

class ApplicantsAdmin(admin.ModelAdmin):
    class Meta:
        model=Applicants
        fields=('applicant','job')
    list_display=('applicant','job')    
admin.site.register(Jobs,JobsAdmin)
admin.site.register(Applicants,ApplicantsAdmin)
admin.site.register(AppliedJobs)
admin.site.register(SavedJobs)
admin.site.register(Selected)
