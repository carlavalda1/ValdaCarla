from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),

    path("cursos/", cursos, name="cursos"),
    path("cursoForm/", cursoForm, name="cursoForm"),
    path("cursoUpdate/<id>/", cursoUpdate, name="cursoUpdate"),
    path("cursoDelete/<id>/", cursoDelete, name="cursoDelete"),

    path("profesores/", profesores, name="profesores"),
    path("profesorForm/", profesorForm, name="profesorForm"),
    path("profesorUpdate/<id>/", profesorUpdate, name="profesorUpdate"),
    path("profesorDelete/<id>/", profesorDelete, name="profesorDelete"),

    path("estudiantes/", estudiantes, name="estudiantes"),
    path("estudianteForm/", estudianteForm, name="estudiantesForm"),
    path("estudianteUpdate/<id>/", estudianteUpdate, name="estudianteUpdate"),
    path("estudianteDelete/<id>/", estudianteDelete, name="estudianteDelete"),
    
    path("entregables/", entregables, name="entregables"),
    path("entregableForm/", entregableForm, name="entregableForm"),
    path("entregableUpdate/<id>/", entregableUpdate, name="entregableUpdate"),
    path("entregableDelete/<id>/", entregableDelete, name="entregableDelete"),

    path("aboutme/", aboutme, name="aboutme")

]