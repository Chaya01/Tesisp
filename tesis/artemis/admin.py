from django.contrib import admin
from .models import Estudiantes, Cursos, Diplomados, Areas,Becas

admin.site.register(Estudiantes)
admin.site.register(Cursos)
admin.site.register(Diplomados)
admin.site.register(Areas)
admin.site.register(Becas)

# Register your models here.
