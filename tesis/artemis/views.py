from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from artemis.forms import Formulario_area
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from artemis.models import Areas, Estudiantes
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from . import views
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render

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
        context['Becas'] = Becas.objects.all()
        return context

#class panel_estudiantes(TemplateView): 
#    template_name = 'panel_estudiantes.html'

### Paneles de administracion ###
class panel_estudiantes(ListView):
    context_object_name = 'panel_estudiantes'
    template_name = 'panel_estudiantes.html'
    paginate_by = 10
    queryset = Estudiantes.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_estudiantes, self).get_context_data(**kwargs)
        context['Estudiantes'] = Estudiantes.objects.all()
        return context

class panel_becas(ListView):
    context_object_name = 'panel_becas'
    template_name = 'panel_becas.html'
    paginate_by = 10
    queryset = Becas.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_becas, self).get_context_data(**kwargs)
        context['Becas'] = Becas.objects.all()
        return context

class panel_periodos(ListView):
    context_object_name = 'panel_periodos'
    template_name = 'panel_periodos.html'
    paginate_by = 10
    queryset = Periodo.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_periodos, self).get_context_data(**kwargs)
        context['Periodo'] = Periodo.objects.all()
        return context

class panel_areas(ListView):
    context_object_name = 'panel_areas'
    template_name = 'panel_areas.html'
    paginate_by = 10
    queryset = Areas.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_areas, self).get_context_data(**kwargs)
        context['Areas'] = Areas.objects.all()
        return context

class panel_profesiones(ListView):
    context_object_name = 'panel_profesiones'
    template_name = 'panel_profesiones.html'
    paginate_by = 10
    queryset = Profesiones.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_profesiones, self).get_context_data(**kwargs)
        context['Profesiones'] = Profesiones.objects.all()
        return context

class panel_docentes(ListView):
    context_object_name = 'panel_docentes'
    template_name = 'panel_docentes.html'
    paginate_by = 10
    queryset = Docentes.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_docentes, self).get_context_data(**kwargs)
        context['Docentes'] = Docentes.objects.all()
        return context

class panel_cursos(ListView):
    context_object_name = 'panel_cursos'
    template_name = 'panel_cursos.html'
    paginate_by = 10
    queryset = Cursos.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_cursos, self).get_context_data(**kwargs)
        context['Cursos'] = Cursos.objects.all()
        return context


### Cruds ### funciones basicas###
### Crud Estudiantes###
class Detalle_estudiante(DetailView):
    model = Estudiantes
    template_name = 'cruds/student_detail.html'

class Crear_estudiante(CreateView):
    model = Estudiantes
    form_class = Estudiantes_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_estudiantes')

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
    success_url = reverse_lazy('artemis:panel_estudiantes')
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
    success_url = reverse_lazy('artemis:panel_estudiantes')

### Becas ###

class Detalle_becas(DetailView):
    model = Becas
    template_name = 'cruds/becas_detail.html'

class Crear_beca(CreateView):
    model = Becas
    form_class = Becas_form
    template_name ='cruds/form.html'
    success_url = reverse_lazy('artemis:panel_becas')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre_beca']
        a = re.search("[a-z]",nombre) #validar nombre
        if not a:
            form.add_error('nombre_beca','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Crear_beca, self).form_valid(form)

class Actualizar_beca(UpdateView):
    model = Becas
    form_class = Becas_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_becas')
    
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre_beca']
        a = re.search("[a-z]",nombre) #validar nombre
        if not a:
            form.add_error('nombre_beca','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Actualizar_beca, self).form_valid(form)

class Borrar_beca(DeleteView):
    model = Becas
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_becas')

### Periodo ###

#class Detalle_periodos(DetailView):
#    model = Periodo
#    template_name ='cruds/periodos_detail.html'

class Crear_periodo(CreateView):
    model = Periodo
    form_class = Periodo_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_periodos')

class Actualizar_periodo(UpdateView):
    model = Periodo
    form_class = Periodo_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_periodos')

class Borrar_periodo(DeleteView):
    model = Periodo
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_periodos')

### Areas ###

class Detalle_area(DetailView):
    model = Areas
    template_name = 'cruds/areas_detail.html'

class Crear_area(CreateView):
    model = Areas
    form_class = Areas_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_areas')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre_area']
        a = re.search("[a-z]",nombre) #validar nombre
        if not a:
            form.add_error('nombre_area','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Crear_area, self).form_valid(form)

class Actualizar_area(UpdateView):
    model = Areas
    form_class = Areas_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_areas')
    
    def form_valid(self, form):
        nombre = form.cleaned_data['nombre_area']
        a = re.search("[a-z]",nombre) #validar nombre
        if not a:
            form.add_error('nombre_area','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Actualizar_area, self).form_valid(form)

class Borrar_area(DeleteView):
    model = Areas
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_areas')

### Profesiones ###

class Detalle_profesiones(DetailView):
    model = Profesiones
    template_name = 'cruds/profesiones_detail.html'

class Crear_profesiones(CreateView):
    model = Profesiones
    form_class = Profesiones_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_profesiones')

    def form_valid(self, form):
        nombre_p = form.cleaned_data['nombre_profesion']
        a = re.search("[a-z]",nombre_p) #validar nombre
        if not a:
            form.add_error('nombre_profesion','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Crear_profesiones, self).form_valid(form)

class Actualizar_profesiones(UpdateView):
    model = Profesiones
    form_class = Profesiones_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_profesiones')

class Borrar_profesiones(DeleteView):
    model = Profesiones
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_profesiones')

### Docentes ###

class Detalle_docentes(DetailView):
    model = Docentes
    template_name = 'cruds/docentes_detail.html'

class Crear_docente(CreateView):
    model = Docentes
    form_class = Docentes_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_docentes')

    def form_valid(self, form):
        rut = form.cleaned_data['rut_docente']
        nombre = form.cleaned_data['nombre_docente']
        apellido = form.cleaned_data['apellido_docente']
        a = re.search("[a-z]$",nombre) #validar nombre
        b = re.search("[a-z]$",apellido) #validar apellido
        x = re.search("[0-9]{8}[0-9kK]{1}$", rut) #validar rut

        if not x:
            form.add_error('rut_docente', 'rut invalido')
            return self.form_invalid(form)
        elif not a:
            form.add_error('nombre_docente', 'el nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('apellido_docente','el apellido solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Crear_docente, self).form_valid(form)

class Actualizar_docente(UpdateView):
    model = Docentes
    form_class = Docentes_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_docentes')

    def form_valid(self, form):
        rut = form.cleaned_data['rut_docente']
        nombre = form.cleaned_data['nombre_docente']
        apellido = form.cleaned_data['apellido_docente']
        a = re.search("[a-z]$",nombre) #validar nombre
        b = re.search("[a-z]$",apellido) #validar apellido
        x = re.search("[0-9]{8}[0-9kK]{1}$", rut) #validar rut

        if not x:
            form.add_error('rut_docente', 'rut invalido')
            return self.form_invalid(form)
        elif not a:
            form.add_error('nombre_docente', 'el nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        elif not b:
            form.add_error('apellido_docente','el apellido solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Actualizar_docente, self).form_valid(form)

class Borrar_docente(DeleteView):
    model = Docentes
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_docentes')

### Cursos ###

class Detalle_cursos(DetailView):
    model = Cursos
    template_name = 'cruds/cursos_detail.html'

class Crear_cursos(CreateView):
    model = Cursos
    form_class = Cursos_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_cursos')

class Actualizar_cursos(UpdateView):
    model = Cursos
    form_class = Cursos_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_cursos')

class Borrar_cursos(DeleteView):
    model = Cursos
    template_name ='cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_cursos')

### Diplomados ###

class Detalle_diplomados(DetailView):
    model = Diplomados
    template_name = 'cruds/diplomados_detail.html'

class Crear_diplomados(CreateView):
    model = Diplomados
    form_class = Cursos_form
    template_name = 'cruds/form.html'
    sucess_url = reverse_lazy('artemis:index')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre_diplomado']
        a = re.search("[a-z]",nombre) #validar nombre
        if not a:
            form.add_error('nombre_diplomado','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Crear_diplomados, self).form_valid(form)

class Actualizar_diplomados(UpdateView):
    model = Diplomados
    form_class = Diplomados_form
    template_name = 'cruds/upadate.html'
    sucess_url = reverse_lazy('artemis:index')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre_diplomado']
        a = re.search("[a-z]",nombre) #validar nombre
        if not a:
            form.add_error('nombre_diplomado','El nombre solo debe contener caracteres alfanumericos')
            return self.form_invalid(form)
        return super(Actualizar_diplomados, self).form_valid(form)

class Borrar_diplomado(DeleteView):
    model = Diplomados
    template_name = 'cruds/delete.html'
    sucess_url= reverse_lazy('artemis:index')

### Matriculas ###

class Detalle_matricula(DetailView):
    model = Matriculas
    template_name = 'cruds/matriculas_detail.html'

class Crear_matricula(CreateView):
    model = Matriculas
    form_class = Matriculas_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:index')

class Actualizar_matricula(UpdateView):
    model = Matriculas
    form_class = Matriculas_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:index')

class Borrar_matricula(DeleteView):
    model = Matriculas
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:index')

### Cuotas ###

class Detalle_cuotas(DetailView):
    model = Cuotas
    template_name = 'cruds/cuotas_detail.html'

class Crear_cuota(CreateView):
    model = Cuotas
    form_class = Cuotas_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:index')

class Actualizar_cuota(UpdateView):
    model = Cuotas
    form_class = Cuotas_form
    template_name = 'cruds/update.html'
    sucess_url = reverse_lazy('artemis:index')

class Borrar_cuota(DeleteView):
    model = Cuotas
    template_name = 'cruds/delete.html'
    sucess_url = reverse_lazy('artemis:index')


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

