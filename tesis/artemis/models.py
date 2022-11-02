from operator import truediv
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Becas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_beca = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_beca

class Areas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_area

class Profesiones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_profesion = models.CharField(max_length=20)
    area_profesion= models.ForeignKey(Areas, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_profesion

class Estudiantes(models.Model):
    rut_estudiante = models.CharField(max_length=20,primary_key=True)
    nombre_estudiante = models.CharField(max_length=30)
    apellido_estudiante = models.CharField(max_length=20)
    num_tel_estudiante = models.IntegerField()
    direccion_estudiante = models.CharField(max_length=30)
    profesion = models.ForeignKey(Profesiones, on_delete= models.CASCADE)
    beca = models.ForeignKey(Becas, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_estudiante

class Docentes(models.Model):
    rut_docente = models.CharField(primary_key=True,max_length=20)
    nombre_docente = models.CharField(max_length=20)
    apellido_docente = models.CharField(max_length=20)
    profesion_docente = models.ForeignKey(Profesiones,on_delete=models.CASCADE)
    num_tel_docente = models.IntegerField()
    def __str__(self):
        return self.nombre_docente

class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=20)
    docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_curso

class Diplomados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_diplomado = models.CharField(max_length=20)
    # cursos_req = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    cursos_req = models.ManyToManyField(Cursos)
    capacidad = models.IntegerField()
    def __str__(self):
        return self.nombre_diplomado

class Inscripciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_inscripcion = models.CharField(max_length=20)
    diplomado = models.ManyToManyField(Diplomados)
    capacidad = models.IntegerField()
    estudiantes = models.ManyToManyField(Estudiantes)
    def __str__(self):
        return self.nombre_inscripcion
