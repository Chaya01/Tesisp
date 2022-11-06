from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError

class Formulario_area(forms.Form):
    id = forms.IntegerField()
    beca = forms.CharField(widget=forms.Textarea)

class Areas_form(forms.ModelForm):
    class Meta:
        model = Areas
        fields = ['id','nombre_area']
        
class Estudiantes_form(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['rut_estudiante','nombre_estudiante','apellido_estudiante','num_tel_estudiante','direccion_estudiante','profesion','beca']
