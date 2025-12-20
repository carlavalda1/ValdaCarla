from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'clases/index.html')

def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "clases/cursos.html", contexto)

def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "clases/profesores.html", contexto)

def estudiantes(request):
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "clases/estudiantes.html", contexto)

def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "clases/entregables.html", contexto)

def cursoForm(request):
    if request.method == "POST":
        miFormulario = CursoForm(request.POST) #Aqui llega toda la info del formulario
        if miFormulario.is_valid():
            curso_nombre = miFormulario.cleaned_data.get("nombre")
            curso_comision = miFormulario.cleaned_data.get("comision")
            curso_profesor = miFormulario.cleaned_data.get("profesor")
            curso = Curso(nombre=curso_nombre, comision=curso_comision, profesor=curso_profesor)
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "clases/cursos.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = CursoForm()

    contexto = { "form": miFormulario}
    return render(request, "clases/cursoForm.html", contexto)

def cursoUpdate(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        miFormulario = CursoForm(request.POST) #Aqui llega toda la info del formulario
        if miFormulario.is_valid():
            curso.nombre = miFormulario.cleaned_data.get("nombre")
            curso.comision = miFormulario.cleaned_data.get("comision")
            curso.profesor = miFormulario.cleaned_data.get("profesor")
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "clases/cursos.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = CursoForm(initial={"nombre": curso.nombre, "comision": curso.comision})

    contexto = { "form": miFormulario}
    return render(request, "clases/cursoForm.html", contexto)

def cursoDelete(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "clases/cursos.html", contexto)

#Profesores
def profesorForm(request):
    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST)
        if miFormulario.is_valid():
            profesor_nombre = miFormulario.cleaned_data.get("nombre")
            profesor_apellido = miFormulario.cleaned_data.get("apellido")
            profesor_email = miFormulario.cleaned_data.get("email")
            profesor_profesion = miFormulario.cleaned_data.get("profesion")
            profesor = Profesor(nombre=profesor_nombre, apellido=profesor_apellido, email=profesor_email, profesion=profesor_profesion)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "clases/profesores.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = ProfesorForm()

    contexto = { "form": miFormulario}
    return render(request, "clases/profesorForm.html", contexto)

def profesorUpdate(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST)
        if miFormulario.is_valid():
            profesor.nombre = miFormulario.cleaned_data.get("nombre")
            profesor.apellido = miFormulario.cleaned_data.get("apellido")
            profesor.email = miFormulario.cleaned_data.get("email")
            profesor.profesion = miFormulario.cleaned_data.get("profesion")
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "clases/profesores.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = ProfesorForm(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "email": profesor.email, "profesion": profesor.profesion})

    contexto = {"form": miFormulario}
    return render(request, "clases/profesorForm.html", contexto)

def profesorDelete(request, id):
    curso = Profesor.objects.get(id=id)
    curso.delete()
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "clases/profesores.html", contexto)

#Estudiantes
def estudianteForm(request):
    if request.method == "POST":
        miFormulario = estudianteForm(request.POST)
        if miFormulario.is_valid():
            estudiante_nombre = miFormulario.cleaned_data.get("nombre")
            estudiante_apellido = miFormulario.cleaned_data.get("apellido")
            estudiante_email = miFormulario.cleaned_data.get("email")
            estudiante = Estudiante(nombre=estudiante_nombre, apellido=estudiante_apellido, email=estudiante_email)
            estudiante.save()
            contexto = {"estudiantes": Estudiante.objects.all()}
            return render(request, "clases/estudiantes.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = ProfesorForm()

    contexto = { "form": miFormulario}
    return render(request, "clases/estudianteForm.html", contexto)

def estudianteUpdate(request, id):
    Estudiante = Estudiante.objects.get(id=id)

    if request.method == "POST":
        miFormulario = estudianteForm(request.POST)
        if miFormulario.is_valid():
            Estudiante.nombre = miFormulario.cleaned_data.get("nombre")
            Estudiante.apellido = miFormulario.cleaned_data.get("apellido")
            Estudiante.email = miFormulario.cleaned_data.get("email")
            Estudiante.save()
            contexto = {"estudiantes": Estudiante.objects.all()}
            return render(request, "clases/estudiantes.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = estudianteForm(initial={"nombre": estudiantes.nombre, "apellido": estudiantes.apellido, "email": estudiantes.email})

    contexto = {"form": miFormulario}
    return render(request, "clases/estudiantesForm.html", contexto)

def estudianteDelete(request, id):
    curso = Estudiante.objects.get(id=id)
    curso.delete()
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "clases/estudiantes.html", contexto)

#Entregable
def entregableForm(request):
    if request.method == "POST":
        miFormulario = entregableForm(request.POST) #Aqui llega toda la info del formulario
        if miFormulario.is_valid():
            entregable_nombre = miFormulario.cleaned_data.get("nombre")
            entregable_comision = miFormulario.cleaned_data.get("comision")
            entregable = Entregable(nombre=entregable_nombre, comision=entregable_comision)
            entregable.save()
            contexto = {"entregables": Entregable.objects.all()}
            return render(request, "clases/entregables.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = entregableForm(initial={"nombre": entregable.nombre, "comision": entregable.comision})

    contexto = { "form": miFormulario}
    return render(request, "clases/entregableForm.html", contexto)

def entregableUpdate(request, id):
    entregable = Entregable.objects.get(id=id)

    if request.method == "POST":
        miFormulario = EntregableForm(request.POST) #Aqui llega toda la info del formulario
        if miFormulario.is_valid():
            entregable.nombre = miFormulario.cleaned_data.get("nombre")
            entregable.comision = miFormulario.cleaned_data.get("comision")
            entregable.save()
            contexto = {"entregables": Entregable.objects.all()}
            return render(request, "clases/entregables.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacio
        miFormulario = entregableForm(initial={"nombre": entregable.nombre, "comision": entregable.comision})

    contexto = { "form": miFormulario}
    return render(request, "clases/entregableForm.html", contexto)

def entregableDelete(request, id):
    entregable = Entregable.objects.get(id=id)
    entregable.delete()
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "clases/entregables.html", contexto)

def aboutme(request):
    return render(request, "clases/aboutme.html")