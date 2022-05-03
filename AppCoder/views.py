from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(self):
    curso=Curso(nombre= "Curso de Django", comision= 12345)
    curso.save()
    texto= f"Curso: {curso.nombre} - Comisión: {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return HttpResponse("Esta es la página de profesores")

def estudiantes(request):
    return HttpResponse("Esta es la página de estudiantes")

def cursos(request):
    return HttpResponse("Esta es la página de cursos")

def entregables(request):
    return HttpResponse("Esta es la página de entregables")