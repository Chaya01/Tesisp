from django.urls import path
#from artemis.views import Crear_area, Borrar_area, Editar_area
from .views import *

app_name = 'artemis'

urlpatterns = [
    path('',index.as_view, name='index'),
    path('Estudiante/<str:pk>', Detalle_estudiante.as_view(), name='student_detail'),
    path('Estudiante/form/', Crear_estudiante.as_view(), name='new_student'),




#    path('areas/add/', Crear_area.as_view(), name='area-add'),
#    path('areas/<int:pk>/', Editar_area.as_view(), name='area-update'),
#    path('areas/<int:pk>/delete/', Borrar_area.as_view(), name='area-delete'),
]