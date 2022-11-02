from django.contrib import admin
from .models import Estudiantes, Cursos, Diplomados, Areas,Becas, Docentes, Profesiones, Inscripciones

admin.site.register(Estudiantes)
admin.site.register(Cursos)
admin.site.register(Diplomados)
admin.site.register(Areas)
admin.site.register(Becas)
admin.site.register(Docentes)
admin.site.register(Profesiones)
admin.site.register(Inscripciones)

# Register your models here.
