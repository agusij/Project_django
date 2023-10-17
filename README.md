# ¡Bienvenidos a la Entrega Jaureguiberry!

## DEMO
[https://drive.google.com/file/d/1PSvWvviIhw6Jt024igGBY6ULAU3ft99i/view?usp=sharing]

## Instalación

### Pre-requisitos:
- Asegúrese de estar en el directorio donde descargó el proyecto.
- Es recomendable, aunque no esencial, utilizar un entorno virtual. Puede crear uno con el siguiente comando:

python -m venv venv-entrega-intermedia


### Pasos:

1. **Activar el entorno virtual (si lo creó anteriormente):**

. start.sh


2. **Instalación de dependencias:**

Asegúrese de tener todas las librerías requeridas. Puede instalarlas con:

pip install -r requirements.txt


## Ejecución

1. **Ejecutar el proyecto:**


python manage.py runserver


Luego, abra su navegador y siga la dirección proporcionada por el servidor.

## Secciones y funcionalidades

1. **Inicio:**
Haga clic en 'Inicio' para regresar a la página principal en cualquier momento.

2. **Secciones principales:**
- **Alias:** Se puede crear un objeto Alias y Followers que luego, se desplega en forma de lista para editar, eliminar y ver mas.
- **Tweets:** Muestra todas las publicaciones. Si eres el autor de una publicación, podrás editarla o eliminarla. Si no lo eres, estas opciones no estarán disponibles. Se intento agregar un boton de likes. Pero como el auto aun no cuenta con amplios conocimientos en js, se tiene que recargar la pagina para ver el total de likes.
- **New Tweet:** Permite publicar un nuevo tweet e imagen.
- **Sobre mí:** Breve descripción sobre el autor.
- **Panel de Cuenta:** Gestión de usuarios incluyendo inicio de sesión, registro, edición de perfil, cambio de contraseña, y más.

3. **Gestión de usuarios:**
Si no está logueado, podrá navegar por el sitio con funcionalidades limitadas. Una vez que inicie sesión, tendrá acceso a 'Mi perfil', 'Editar perfil', y otras opciones de personalización de usuario.

4. **Barra para buscar tweets:** En esta barra puedes buscar cualquier tweet publicado, si no se encuentra saldra un cartel que dice 'Resultados de búsqueda para: XXX, No se encontraron tweets que coincidan con tu búsqueda.'





