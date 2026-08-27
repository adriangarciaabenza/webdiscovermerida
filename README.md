# WebDiscoverMerida

Aplicacion web minima en Flask que muestra `Hello, World!` y permite descubrir
Mérida, su legado romano y cinco lugares para visitar.

## Requisitos

- Python 3.12 o superior.

## Instalacion y ejecucion con uv

Ejecuta los comandos desde el directorio `WebDiscoverMerida`:

```bash
uv venv .venv
source .venv/bin/activate
uv pip install --python .venv/bin/python -r requirements.txt
flask --app app run
```

Abre http://127.0.0.1:5000/ en el navegador. El servidor sirve la ruta `/` y
renderiza la pagina de bienvenida. El enlace `Descubre Mérida` lleva a `/merida`.

Como alternativa, puedes crear y preparar el entorno con Python y pip:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
flask --app app run
```

## Delegacion de tareas

La implementacion se delega en tareas pequenas al subagente `local-worker`,
configurado para usar el modelo local `lmstudio/google/gemma-4-e4b`. Desde este
directorio, cada tarea debe invocarse explicitamente con:

```bash
opencode run --agent local-worker "Describe una tarea pequena y aislada"
```

No debe usarse un subagente generico como `general` o `explore` para implementar
estas tareas. Cada resultado se revisa y se prueba antes de continuar.

## Pruebas

Con el entorno virtual activado, ejecuta:

```bash
.venv/bin/python -m pytest
```

El archivo `tests/test_app.py` verifica las rutas `/` y `/merida`, el enlace de
navegacion, los lugares destacados y las imagenes locales.

## Despliegue en Render

El archivo `render.yaml` configura un Web Service Python. Render instala las
dependencias con `pip install -r requirements.txt` y arranca Flask mediante
Gunicorn en el puerto que proporciona la variable `PORT`.

## Estructura y alcance

- `app.py`: crea la aplicacion Flask y define la ruta `/`.
- `templates/index.html`: plantilla de la pagina principal.
- `templates/merida.html`: pagina informativa sobre Mérida y su legado romano.
- `static/styles.css`: estilos de la pagina.
- `specs/merida-content.md`: contenido historico aprobado para la feature.
- `specs/merida-visit-content.md`: contenido turistico, fuentes y licencia de
  las ilustraciones.
- `static/images/`: fotografias locales con licencia Creative Commons y sus
  atribuciones documentadas en `specs/merida-visit-content.md`.
- `requirements.txt`: dependencias fijadas de Flask y pytest.
- `specs/`: documentos de constitucion, stack tecnologico y roadmap.

El alcance son dos paginas ejecutadas localmente. No incluye base de datos,
autenticacion, API adicional ni persistencia.

## Especificaciones

- [Constitucion](specs/constitution.md): principios y criterios de calidad.
- [Stack tecnologico](specs/tech-stack.md): herramientas y versiones objetivo.
- [Roadmap](specs/roadmap.md): entregas pequenas y verificables.
