from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from artemis.forms import Formulario_area
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from artemis.models import Areas, Estudiantes
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from . import views
from .forms import *

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class index(ListView):
    context_object_name = 'index'
    template_name = 'index.html'
    queryset = Estudiantes.objects.all()

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['Estudiantes'] = Estudiantes.objects.all()
        return context

### Cruds ###
### Crud Estudiantes###
class Detalle_estudiante(DetailView):
    model = Estudiantes
    template_name = 'cruds/student_detail.html'

class Crear_estudiante(CreateView):
    model = Estudiantes
    form_class = Estudiantes_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:index')

    def form_valid(self, form):
        rut = form.cleaned_data['rut_estudiante']
        nombre = form.cleaned_data['nombre_estudiante']
        apellido = form.cleaned_data['apellido_estudiante']
        a = re.search("[a-z]$",nombre) #validar nombre
        b = re.search("[a-z]$",apellido) #validar apellido
        x = re.search("[0-9]{8}[0-9kK]{1}$", rut) #validar rut

        if not x:
            form.add_error('rut_estudiante', 'rut invalido')
            return self.form_invalid(form)
        elif not a:
            form.add_error('nombre_estudiante', 'el nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('apellido_estudiante','el apellido solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Crear_estudiante, self).form_valid(form)
    
class Actualizar_estudiante(UpdateView):
    model = Estudiantes
    form_class = Estudiantes_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:index')
    #fields = ['rut', 'nombre','apellido','area', 'correo', 'telefono']

    #validamos que el formulario sea valido
    def form_valid(self, form):
        rut = form.cleaned_data['rut_estudiante']
        nombre = form.cleaned_data['nombre_estudiante']
        apellido = form.cleaned_data['apellido_estudiante']
        a = re.search("[a-z]$",nombre) #validar nombre
        b = re.search("[a-z]$",apellido) #validar apellido
        x = re.search("[0-9]{8}[0-9kK]{1}$", rut) #validar rut

        if not x:
            form.add_error('rut_estudiante', 'rut invalido')
            return self.form_invalid(form)
        elif not a:
            form.add_error('nombre_estudiante', 'el nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('apellido_estudiante','el apellido solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Actualizar_estudiante, self).form_valid(form)

class Borrar_estudiante(DeleteView):
    model = Estudiantes
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:index')





#class Vista_areas(FormView):
#   template_name = 'contact.html'
#   form_class = Formulario_area
#   success_url = '/thanks/'

#class Crear_area(CreateView):
#   model = Areas
#   fields = ['nombre_area']

#class Editar_area(UpdateView):
#   model = Areas
#   fields = ['nombre_area']

#class Borrar_area(DeleteView):
#   model = Areas
#   success_url = reverse_lazy('author-list')

