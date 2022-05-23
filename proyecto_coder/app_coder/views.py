from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso

# Create your views here.

def curso(request):
    cursos= Curso.objects.all()
    return HttpResponse(cursos)

