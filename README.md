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

Dentro de la carperta de la aplicación inicio estarán los archivos:
- Models: En este se define la estructura de la tabla Articulo (campos articulo y marca).
- Urls: Mapea las URL como /crear-articulo/... y /listado-articulos a sus funciones correspondientes en views.py.
- Views:Contiene las funciones  crear_articulo y listar_articulo.
- Carpeta templates. Dentro de la cual tendremos los archivos:
    - crear_articulo.html
    - listar_articulo.html

Una vez ejecutado el proyecto con el comando python manage.py runserver:
- Con el link http://127.0.0.1:8000/crear-articulo/<articulo>/<marca> podemos sumar artículos a la lista 
- Con el link http://127.0.0.1:8000/listado-articulos podemos ver la lista de artículos generada