from django import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
    path('cursos/', cursos, name='cursos'),
]