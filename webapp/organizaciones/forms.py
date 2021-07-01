from .models import OrgProfile 
from django import forms


class OrgEditForm(forms.ModelForm):
    class Meta:
        model = OrgProfile
        fields = ('nombre', 'ruc','descripcion','imagen','website','direccion','telefono')