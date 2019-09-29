from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Curso
from .forms import ContatoCurso

def curso(request):
    cursos = Curso.objects.all()
    template_name = "layout/curso.html"
    context = {
        'cursos' : cursos
    }
    return render(request, template_name, context)

#def detalhe(request, pk):
#    curso = Curso.objects.get(pk=pk)
#    context = {
#        'curso' : curso
#    }
#    template_name = 'layout/detalhe.html'
 #   return render(request, template_name, context)

def detalhe(request, slug):
    curso = get_object_or_404(Curso, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContatoCurso(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(curso)
            #if form.cleaned_data['question']:
                
            form = ContatoCurso()
            
    else:
        form = ContatoCurso()
    context['form'] = form
    context['curso'] = curso
    template_name = 'layout/detalhe.html'
    return render(request, template_name, context)
