from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Buscar...'}))

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
        
        widgets ={
            'profesion' : forms.Select(attrs={'class': 'form-control'}),
            'beca' : forms.Select(attrs={'class': 'form-control'}),
        }   

class Becas_form(forms.ModelForm):
    class Meta:
        model = Becas
        fields = ['id','nombre_beca']

class Periodo_form(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['id','nombre_periodo','fecha_inicio','fecha_termino','activo']

        widgets = {
            'fecha_inicio' : forms.DateInput(format="%Y-%m-%d",
                                            attrs = {'type':'date','class':'form-control dtpicker', 'required': 'true'}),
            'fecha_termino' : forms.DateInput(format="%Y-%m-%d",
                                            attrs = {'type':'date','class':'form-control dtpicker', 'required': 'true'}),
        }

class Profesiones_form(forms.ModelForm):
    class Meta:
        model = Profesiones
        fields = ['id','nombre_profesion','area_profesion']

        widgets ={
            'area_profesion' : forms.Select(attrs={'class': 'form-control'}),
        }

class Docentes_form(forms.ModelForm):
    class Meta:
        model = Docentes
        fields = ['rut_docente','nombre_docente','apellido_docente','profesion_docente','num_tel_docente']

        widgets ={
            'profesion_docente' : forms.Select(attrs={'class': 'form-control'}),
        }

class Cursos_form(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['id','nombre_curso','docente']

        widgets ={
            'docente' : forms.Select(attrs={'class': 'form-control'}),
        }
class Diplomados_form(forms.ModelForm):
    class Meta:
        model = Diplomados
        fields = ['id','nombre_diplomado','cursos_req','capacidad','precio']

        widgets={
            'cursos_req' : forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input','type':'radio'})
        }

class Matriculas_form(forms.ModelForm):
    class Meta:
        model = Matriculas
        fields = ['diplomado','estudiantes','activo','num_cuotas']

        widgets ={
            'diplomado' : forms.Select(attrs={'class': 'form-control'}),
            'estudiantes' : forms.Select(attrs={'class': 'form-control'}),
            'activo' : forms.Select(attrs={'class': 'form-control'}),
        }

class Cuotas_form(forms.ModelForm):
    class Meta:
        model = Cuotas
        fields = ['id','cuotas_por_pagar','fecha_exp','pagado','fecha_pago','monto_pago','numero_cuota']
