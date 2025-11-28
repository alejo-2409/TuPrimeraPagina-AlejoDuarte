## Video de presentación del proyecto
https://drive.google.com/file/d/1T2QhpkvCuTHy3AM3kgJP3kiLyxgAiKfQ/view?usp=sharing

# Mi Catálogo de Artículos de Limpieza 
Página web de catálogo y gestión de artículos de limpieza construida con el framework web Django.


Tecnologías Utilizadas
**Python**

**Django** (Framework web)

**SQLite** (Base de datos por defecto para desarrollo)

**HTML** (Para las plantillas)

## Para que el proyecto funcione correctamente ver el archivo requirements.txt donde se encontrarán las aplicaciones necesarias para el entorno virtual a utilizar.

Para ejecutar las migraciones de Django para crear las tablas en la base de datos db.sqlite3 hay que utilizar los comandos:
    python manage.py makemigrations
    python manage.py migrate

En la carpeta del proyecto llamada PrimeraPagina estarán las configuraciones necesarias en el archivo settings.py y en el archivo urls.py están las rutas que va a seguir el server a la hora de ejecutarse.

## ✨ Características Principales y Requisitos Cumplidos

* **Autenticación Completa:** Incluye vistas de Login, Logout y Registro para usuarios.
* **Vistas Basadas en Clases (CBV):** Uso de CBV (ListView, CreateView, etc.) para el manejo del modelo principal.
* **Seguridad:** Implementación de **LoginRequiredMixin** para proteger vistas sensibles (edición, creación, borrado) y uso de decoradores en vistas comunes.
* **Modelo Principal:** Modelo `Articulo` con 3 campos de texto (o número) y 1 campo de imagen.
* **Herencia de Templates:** Uso de `base.html` para un diseño consistente.
* **CRUD Funcional:** Implementación completa de las 5 vistas para gestión del modelo.
