from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LogoutView
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

    path("estudiantes/", EstudianteListView.as_view(), name="estudiantes"),
    path("estudianteCreate/", EstudianteCreateView.as_view(), name="estudianteCreate"),
    path("estudianteUpdate/<int:pk>/", EstudianteUpdateView.as_view(), name="estudianteUpdate"),
    path("estudianteDelete/<int:pk>/", EstudianteDeleteView.as_view(), name="estudianteDelete"),

    path("entregables/", entregables, name="entregables"),
    path("entregableForm/", entregableForm, name="entregableForm"),
    path("entregableUpdate/<id>/", entregableUpdate, name="entregableUpdate"),
    path("entregableDelete/<id>/", entregableDelete, name="entregableDelete"),
   
    path("aboutme/", aboutme, name="aboutme"),

    #Buscar
    path("buscarCursos/", buscarCursos, name="buscarCursos"),
    path("encontrarCursos/", encontrarCursos, name="encontrarCursos"),

    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", register, name="register"),
    path("perfil/", perfil, name="perfil"),
    path("avatar/", avatar, name="avatar"), 
    
    ]