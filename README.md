
# Proyecto: Mi Primera Página Web

Este proyecto es una aplicación web desarrollada en Django que simula un sistema de gestión académica. El sitio cuenta con varias pestañas: **Inicio**, **Cursos**, **Profesores**, **Estudiantes**, **Entregas** y **About Me**. Cada una de estas secciones está pensada para permitir operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre diferentes entidades. Aunque estas funcionalidades no se muestran en la interfaz gráfica, sí están implementadas en el código.

## Estructura del Sitio
- **Inicio**: Página principal.
- **Cursos**: Gestión de cursos (agregar, modificar, eliminar).
- **Profesores**: Gestión de profesores (agregar, modificar, eliminar).
- **Estudiantes**: Gestión de estudiantes (agregar, modificar, eliminar).
- **Entregas**: Gestión de entregas (agregar, modificar, eliminar).
- **About Me**: Información sobre el autor.

## Funcionalidades Implementadas
En cada sección (Cursos, Profesores, Estudiantes, Entregas) se pueden realizar las siguientes operaciones:
- **Agregar**: Crear un nuevo registro.
- **Modificar**: Editar datos como nombre o número de comisión.
- **Eliminar**: Borrar registros existentes.

Estas funcionalidades están implementadas en el código (vistas, modelos y URLs)

## Orden para Probar
1. Acceder a la página de **Inicio**.
2. Probar la gestión de **Cursos**:
   - Agregar un curso.
   - Modificar nombre o comisión.
   - Eliminar curso.
3. Probar la gestión de **Profesores**.
4. Probar la gestión de **Estudiantes**.
5. Probar la gestión de **Entregas**.
6. Revisar la pestaña **About Me**.

## Ubicación de las Funcionalidades en el Código
- **Modelos**: `clases/models.py`
- **Vistas**: `clases/views.py`
- **URLs**: `clases/urls.py`
- **Templates**: `clases/templates/clases/`
- **Configuración del proyecto**: `miprimerapaginavalda/settings.py`
