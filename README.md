# Proyecto: Mi Primera Pagina Web

Este proyecto es una aplicación web desarrollada en **Django** que simula un sistema de gestión académica con funcionalidades adicionales para la gestión de usuarios. El sitio cuenta con varias pestañas: **Inicio**, **Cursos**, **Profesores**, **Estudiantes**, **Entregables**, **Acerca de mí**, además de mostrar el **nombre de usuario**, **nombre y apellido**, y el **avatar** del usuario autenticado. También incluye botones para **loguearse** y **desloguearse**.

---

## Estructura del Sitio
- **Inicio**: Página principal del sitio.
- **Cursos**: Gestión de cursos (agregar, modificar, eliminar).
- **Profesores**: Gestión de profesores (agregar, modificar, eliminar).
- **Estudiantes**: Gestión de estudiantes (agregar, modificar, eliminar).
- **Entregables**: Gestión de entregas (agregar, modificar, eliminar).
- **Acerca de mí**: Información sobre el autor.
- **Usuario**: Visualización del nombre de usuario, nombre completo y avatar.
- **Autenticación**: Botones para iniciar y cerrar sesión.

---

## Funcionalidades Implementadas
En cada sección (Cursos, Profesores, Estudiantes, Entregables) se pueden realizar las siguientes operaciones:
- **Agregar**: Crear un nuevo registro.
- **Modificar**: Editar datos como nombre o número de comisión.
- **Eliminar**: Borrar registros existentes.

Además:
- **Autenticación**: Sistema de login/logout implementado.
- **Perfil de Usuario**:
  - Visualización del avatar, nombre y apellido del usuario autenticado.
  - **Posibilidad de modificar el avatar** desde la interfaz del perfil.
- **Panel de Administración**:
  - Acceso al panel
  - Permite gestionar todas las entidades del sistema (Cursos, Profesores, Estudiantes, Entregables).
  - Administración de usuarios y permisos.
  - Modificación de datos directamente desde la interfaz administrativa.

Para usar el panel, es necesario crear un **superusuario**

## Orden para Probar
1. Acceder a la página de **Inicio**.
2. Probar el sistema de **Autenticación**:
   - Loguearse con un usuario válido.
   - Verificar la visualización del nombre, apellido y avatar.
3. Probar la gestión de **Cursos**:
   - Agregar un curso.
   - Modificar nombre o comisión.
   - Eliminar curso.
4. Probar la gestión de **Profesores**.
5. Probar la gestión de **Estudiantes**.
6. Probar la gestión de **Entregables**.
7. Revisar la pestaña **Acerca de mí**.
8. Modificar el avatar desde el perfil del usuario.
9. Acceder al **panel de administración** para gestionar entidades y usuarios.
10. Desloguearse.

---

## Ubicación de las Funcionalidades en el Código
- **Modelos**: `clases/models.py`
- **Vistas**: `clases/views.py`
- **URLs**: `clases/urls.py`
- **Templates**: `clases/templates/clases/`
- **Configuración del proyecto**: `miprimerapaginavalda/settings.py`
- **Autenticación y Perfil**: `usuarios/` (modelos, vistas y templates relacionados)

Link de Google Drive con video que muestra la página y sus funcionalidades:(https://drive.google.com/drive/u/0/folders/1yarwdNyb6yE4qNtQW95kmJPWLIXDJUCP)
