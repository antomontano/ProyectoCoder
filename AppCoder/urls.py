from django import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio),
    path('profesores/', profesores),
    path('estudiantes', estudiantes),
    path('entregables', entregables),
    path('cursos/', cursos),
]