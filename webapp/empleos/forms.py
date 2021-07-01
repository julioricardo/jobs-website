from django import forms
from .models import Jobs, Applicants
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'


class NewJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['titulo','tipo','categoria','zona','ciudad','salario','descripcion','fecha_cierre']
        widgets = {
            'fecha_cierre': DateInput(),
            
        }

    def clean_last_date(self):
        date = self.cleaned_data["last_date"]
        if date.date() < datetime.now().date():
            raise ValidationError("Last date can't be before from today")
        return date

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model=Applicants
        fields=['cv','cp']

    
class EditJobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['titulo','tipo','categoria','zona','ciudad','salario','descripcion','fecha_cierre']
        widgets = {
            'fecha_cierre': DateInput(),
            
        }
    def clean_last_date(self):
        date = self.cleaned_data["last_date"]
        if date.date() < datetime.now().date():
            raise ValidationError("Last date can't be before from today")
        return date    