from django.urls import URLPattern, path
from . import views
URLPattern= [
    path("cursos", views.cursos)
]