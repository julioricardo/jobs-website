
from django import forms
from .models import Profile

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('cedula','direccion','telefono','imagen','ods','descripcion')
