from django.contrib import admin
from .models import OrgProfile, User
# Register your models here.

class OrgProfileAdmin(admin.ModelAdmin):
    def get_email(self, obj):
        return obj.user.email
    readonly_fields=('creado','modificado')
    list_display=('get_email','nombre')
    class Meta:
        model = OrgProfile
        
    

admin.site.register(OrgProfile,OrgProfileAdmin)