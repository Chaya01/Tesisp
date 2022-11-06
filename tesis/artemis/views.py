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
class Detalle_estudiante(DetailView):
    model = Estudiantes
    template_name = 'student_detail.html'

class Crear_estudiante(CreateView):
    model = Estudiantes
    form_class = Estudiantes_form
    template_name = 'form.html'
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

