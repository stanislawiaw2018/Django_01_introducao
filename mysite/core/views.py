from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato

def home(request):
    return render(request,"layout/index.html")

def contato(request):
    return render(request,"layout/contato.html")
# Create your views here.
