from django.urls import path
#from artemis.views import Crear_area, Borrar_area, Editar_area
from .views import *

app_name = 'artemis'

urlpatterns = [
    ###paneles ###
    path('',index.as_view(), name='index'),
    path('panel_estudiantes.html',panel_estudiantes.as_view(),name ='panel_estudiantes'),
    path('panel_becas.html',panel_becas.as_view(),name='panel_becas'),
    path('panel_periodos.html',panel_periodos.as_view(),name = 'panel_periodos'),
    path('panel_areas.html',panel_areas.as_view(),name = 'panel_areas'),
    path('panel_profesiones.html',panel_profesiones.as_view(),name = 'panel_profesiones'),
    path('panel_docentes.html',panel_docentes.as_view(),name = 'panel_docentes'),
    path('panel_cursos.html',panel_cursos.as_view(),name = 'panel_cursos'),
    path('panel_diplomados.html',panel_diplomados.as_view(),name = 'panel_diplomados'),
    path('panel_matriculas.html',panel_matriculas.as_view(),name ='panel_matriculas'),

    ### Funciones ###
    path('Estudiantes/<str:pk>', Detalle_estudiante.as_view(), name='student_detail'),
    path('Estudiantes/form/', Crear_estudiante.as_view(), name='new_student'),
    path('Estudiantes/update/<str:pk>', Actualizar_estudiante.as_view(), name='edit_student'),
    path('Estudiantes/delete/<str:pk>', Borrar_estudiante.as_view(), name='delete_student'),

    path('Becas/<str:pk>', Detalle_becas.as_view(), name='becas_detail'),
    path('Becas/form/', Crear_beca.as_view(), name='new_beca'),
    path('Becas/update/<str:pk>', Actualizar_beca.as_view(), name='edit_beca'),
    path('Becas/delete/<str:pk>', Borrar_beca.as_view(), name='delete_beca'),

    path('Periodo/form/', Crear_periodo.as_view(), name='new_periodo'),
    path('Periodo/update/<str:pk>', Actualizar_periodo.as_view(), name='edit_periodo'),
    path('Periodo/delete/<str:pk>', Borrar_periodo.as_view(), name='delete_periodo'),

    path('Areas/form/', Crear_area.as_view(), name='new_area'),
    path('Areas/update/<str:pk>', Actualizar_area.as_view(), name='edit_area'),
    path('Areas/delete/<str:pk>', Borrar_area.as_view(), name='delete_area'),

    path('Profesiones/form/', Crear_profesiones.as_view(), name='new_profesion'),
    path('Profesiones/update/<str:pk>', Actualizar_profesiones.as_view(), name='edit_profesion'),
    path('Profesiones/delete/<str:pk>', Borrar_profesiones.as_view(), name='delete_profesion'),

    path('Docentes/form/', Crear_docente.as_view(), name='new_docente'),
    path('Docentes/update/<str:pk>', Actualizar_docente.as_view(), name='edit_docente'),
    path('Docentes/delete/<str:pk>', Borrar_docente.as_view(), name='delete_docente'),

    path('Cursos/form/', Crear_cursos.as_view(), name='new_curso'),
    path('Cursos/update/<str:pk>', Actualizar_cursos.as_view(), name='edit_curso'),
    path('Cursos/delete/<str:pk>', Borrar_cursos.as_view(), name='delete_curso'),

    path('Diplomados/form/', Crear_diplomados.as_view(), name='new_diplomado'),
    path('Diplomados/update/<str:pk>', Actualizar_diplomados.as_view(), name='edit_diplomado'),
    path('Diplomados/delete/<str:pk>', Borrar_diplomado.as_view(), name='delete_diplomado'),

    path('Matriculas/form/', Crear_matricula.as_view(), name='new_matricula'),
    path('Matriculas/update/<str:pk>', Actualizar_matricula.as_view(), name='edit_matricula'),
    path('Matriculas/delete/<str:pk>', Borrar_matricula.as_view(), name='delete_matricula'),


#    path('areas/add/', Crear_area.as_view(), name='area-add'),
#    path('areas/<int:pk>/', Editar_area.as_view(), name='area-update'),
#    path('areas/<int:pk>/delete/', Borrar_area.as_view(), name='area-delete'),
]