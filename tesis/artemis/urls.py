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

    ### Funciones ###
    path('Estudiantes/<str:pk>', Detalle_estudiante.as_view(), name='student_detail'),
    path('Estudiantes/form/', Crear_estudiante.as_view(), name='new_student'),
    path('Estudiantes/update/<str:pk>', Actualizar_estudiante.as_view(), name='edit_student'),
    path('Estudiantes/delete/<str:pk>', Borrar_estudiante.as_view(), name='delete_student'),

    path('Becas/<str:pk>', Detalle_becas.as_view(), name='becas_detail'),
    path('Becas/form/', Crear_beca.as_view(), name='new_beca'),
    path('Becas/update/<str:pk>', Actualizar_beca.as_view(), name='edit_beca'),
    path('Becas/delete/<str:pk>', Borrar_beca.as_view(), name='delete_beca'),

#    path('Periodo/<str:pk>', Detalle_periodos.as_view(), name='periodos_detail'),
    path('Periodo/form/', Crear_periodo.as_view(), name='new_periodo'),
    path('Periodo/update/<str:pk>', Actualizar_periodo.as_view(), name='edit_periodo'),
    path('Periodo/delete/<str:pk>', Borrar_periodo.as_view(), name='delete_periodo'),

#    path('Areas/<str:pk>', Detalle_areas.as_view(), name='areas_detail'),
    path('Areas/form/', Crear_area.as_view(), name='new_area'),
    path('Areas/update/<str:pk>', Actualizar_area.as_view(), name='edit_area'),
    path('Areas/delete/<str:pk>', Borrar_area.as_view(), name='delete_area'),



#    path('areas/add/', Crear_area.as_view(), name='area-add'),
#    path('areas/<int:pk>/', Editar_area.as_view(), name='area-update'),
#    path('areas/<int:pk>/delete/', Borrar_area.as_view(), name='area-delete'),
]