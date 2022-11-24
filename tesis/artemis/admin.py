from django.contrib import admin
from .models import Estudiantes, Cursos, Diplomados, Areas,Becas, Docentes, Profesiones, Periodo, Matriculas, Cuotas

admin.site.register(Estudiantes)
admin.site.register(Cursos)
admin.site.register(Diplomados)
admin.site.register(Areas)
admin.site.register(Becas)
admin.site.register(Docentes)
admin.site.register(Profesiones)
admin.site.register(Matriculas)
admin.site.register(Cuotas)
admin.site.register(Periodo)

# Register your models here.