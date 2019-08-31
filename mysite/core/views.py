from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato

def home(request):
    nome =  "Antonio Stanislaw"
    contatos = Contato.objects.all()
    return render(request,"layout/base.html",{'contatos': contatos})

# Create your views here.
