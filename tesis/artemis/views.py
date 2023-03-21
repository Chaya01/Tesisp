from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.edit import FormView
from artemis.forms import Formulario_area
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from artemis.models import Areas, Estudiantes
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from . import views
from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Matriculas_form
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect

### Funciones ###

#funciones de login

# registro
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro Exitoso." )
			return redirect("artemis:index")
		messages.error(request, "Registro Fallido. Informacion no valida.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

# Login
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("artemis:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

#Funciones suplementarias
def crear_cuotas(numero_cuotas:int, payload):
    objetos_a_crear = []
    for cuotas in range(numero_cuotas):
        objetos_a_crear.append = Cuotas(
            cuotas_por_pagar=payload,
            monto_pago = int(payload.precio/numero_cuotas),
            numero_cuota = cuotas
            )
    res = Cuotas.objects.bulk_create(objetos_a_crear)

    return res
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

class panel_diplomados(ListView):
    context_object_name = 'panel_diplomados'
    template_name = 'panel_diplomados.html'
    paginate_by = 10
    queryset = Diplomados.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_diplomados, self).get_context_data(**kwargs)
        context['Diplomados'] = Diplomados.objects.all()
        context['Cursos'] = Cursos.objects.all()
        return context

class panel_matriculas(ListView):
    context_object_name = 'panel_matriculas'
    template_name = 'panel_matriculas.html'
    paginate_by = 10
    queryset = Matriculas.objects.all()
    def get_context_data(self, **kwargs):
        context = super(panel_matriculas, self).get_context_data(**kwargs)
        context['Matriculas'] = Matriculas.objects.all()
        context['Diplomados'] = Diplomados.objects.all()
        context['Estudiantes'] = Estudiantes.objects.all()
        return context
    
class listado_cuotas(ListView):
    model = Cuotas
    template_name = 'listado_cuotas.html'
    context_object_name = 'cuotas'
    paginate_by = 10

    def get_queryset(self):
        # Retrieve the user ID from the URL parameter
        matricula_id  = self.kwargs.get('pk')
#        print("User ID:", matricula_id) print query data

        # Return a queryset of all Cuotas objects that belong to the user
        return Cuotas.objects.filter(cuotas_por_pagar_id=matricula_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Define a lambda function to get the display value of 'pagado'
        get_pagado_display = lambda cuota: 'Pagado' if cuota.pagado else 'No pagado'
        # Use a list comprehension to get the display value of 'pagado' for each object
        pagado_display_list = [get_pagado_display(cuota) for cuota in context['cuotas']]
        # Add the 'pagado_display_list' to the context
        context['pagado_display_list'] = pagado_display_list
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
    form_class = Diplomados_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_diplomados')

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
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_diplomados')

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
    success_url= reverse_lazy('artemis:panel_diplomados')

### Matriculas ###

class Detalle_matricula(DetailView):
    model = Matriculas
    template_name = 'cruds/matriculas_detail.html'

class Crear_matricula(CreateView):
    model = Matriculas
    form_class = Matriculas_form
    template_name = 'cruds/form.html'
    success_url = reverse_lazy('artemis:panel_matriculas')

    def form_valid(self, form):
        # Create the Matriculas object
        response = super().form_valid(form)

        # Retrieve the Matriculas object
        matricula = self.object

        # Create the payments
        self.create_payments(matricula.id, matricula.num_cuotas)

        # Return the response
        return response

    def create_payments(self, matricula_id, num_payments):
        # Retrieve the Matriculas object
        matricula = Matriculas.objects.get(pk=matricula_id)
        # Retrieve Diplomados objects
        diplomado = matricula.diplomado # assuming only one diploma is associated with a Matriculas object

        fecha_exp = datetime.today() + relativedelta(months=1)

        # Create the specified number of payments
        for i in range(num_payments):
            # Calculate the payment amount (for example, divide the total cost by the number of payments)
            payment_amount = diplomado.precio / matricula.num_cuotas
            # Create a new payment object and associate it with the Matriculas object
#            payment = Cuotas.objects.create(cuotas_por_pagar=matricula, monto_pago=payment_amount, numero_cuota=i+1)
            payment = Cuotas.objects.create(cuotas_por_pagar=matricula, monto_pago=payment_amount, numero_cuota=i+1, fecha_emision=datetime.today(), fecha_exp=fecha_exp)
            fecha_exp += relativedelta(months=1)

class Actualizar_matricula(UpdateView):
    model = Matriculas
    form_class = Matriculas_form
    template_name = 'cruds/update.html'
    success_url = reverse_lazy('artemis:panel_matriculas')

class Borrar_matricula(DeleteView):
    model = Matriculas
    template_name = 'cruds/delete.html'
    success_url = reverse_lazy('artemis:panel_matriculas')

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
    success_url = reverse_lazy('artemis:listado_cuotas')

    def set_pagado(self):
        # Retrieve the instance being updated
        instance = self.get_object()
        # Set the 'pagado' field to True    
        instance.pagado = True
        # Save the updated instance
        instance.save()

    def form_valid(self, form):
        # Call set_pagado() before saving the form data
        self.set_pagado()
        return super().form_valid(form)

class Borrar_cuota(DeleteView):
    model = Cuotas
    template_name = 'cruds/delete.html'
    sucess_url = reverse_lazy('artemis:index')

def pagar_cuota(request, pk):
    cuota = get_object_or_404(Cuotas, pk=pk)
    matricula = cuota.cuotas_por_pagar
    cuota.pagado = True
    cuota.save()
    return redirect('artemis:listado_cuotas', pk=matricula.id)

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

