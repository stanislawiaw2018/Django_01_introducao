from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

def curso(request):
    cursos = Curso.objects.all()
    template_name = "layout/curso.html"
    context = {
        'cursos' : cursos
    }
    return render(request, template_name, context)

def detalhe(request, pk):
    curso = Curso.objects.get(pk=pk)
    context = {
        'curso' : curso
    }
    template_name = 'layout/detalhe.html'
    return render(request, template_name, context)
