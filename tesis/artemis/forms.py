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

class Becas_form(forms.ModelForm):
    class Meta:
        model = Becas
        fields = ['id','nombre_beca']

class Periodo_form(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['id','nombre_periodo','fecha_inicio','fecha_termino','activo']

        widgets = {
            'fecha_inicio' : forms.DateInput(format="%d/%m/%Y",
                                            attrs = {'type':'date','class':'form-control dtpicker', 'required': 'true'}),
            'fecha_termino' : forms.DateInput(format="%d/%m/%Y",
                                            attrs = {'type':'date','class':'form-control dtpicker', 'required': 'true'}),
        }

class Profesiones_form(forms.ModelForm):
    class Meta:
        model = Profesiones
        fields = ['id','nombre_profesion','area_profesion']

class Docentes_form(forms.ModelForm):
    class Meta:
        model = Docentes
        fields = ['rut_docente','nombre_docente','apellido_docente','profesion_docente','num_tel_docente']

class Cursos_form(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['id','nombre_curso','docente']

class Diplomados_form(forms.ModelForm):
    class Meta:
        model = Diplomados
        fields = ['id','nombre_diplomado','cursos_req','capacidad','precio']

        widgets={
            'cursos_req' : forms.CheckboxSelectMultiple(),
        }

class Matriculas_form(forms.ModelForm):
    class Meta:
        model = Matriculas
        fields = ['id','nombre_inscripcion','diplomado','capacidad','estudiantes','activo','num_cuotas']

        widgets ={
            'diplomado' : forms.CheckboxSelectMultiple(),
        }

class Cuotas_form(forms.ModelForm):
    class Meta:
        fields = ['id','cuotas_por_pagar','fecha_emision','fecha_exp','pagado','fecha_pago','monto_pago','numero_cuota']
