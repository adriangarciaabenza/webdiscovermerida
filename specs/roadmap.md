# Roadmap de WebDiscoverMerida

## Fase 1: Especificacion

- [x] Definir la mision y los principios del proyecto.
- [x] Elegir un stack pequeno y reproducible.
- [x] Documentar estructura, alcance y criterios de aceptacion.

## Fase 2: Esqueleto ejecutable

- [x] Crear `requirements.txt` con Flask y pytest.
- [x] Crear `app.py` con una ruta `GET /`.
- [x] Crear la plantilla HTML y los estilos basicos.
- [x] Documentar instalacion y arranque en el README.

**Salida:** la aplicacion arranca localmente y muestra el saludo.

## Fase 3: Verificacion

- [x] Anadir una prueba para `GET /`.
- [x] Comprobar el codigo de respuesta y el texto visible.
- [ ] Probar la instalacion desde un entorno virtual limpio.

**Salida:** todos los criterios constitucionales se pueden comprobar de forma
automatizada o siguiendo pasos documentados.

## Flujo de implementacion

Cada fase de implementacion seguira este ciclo:

1. Descomponer el trabajo pendiente en una tarea pequena y aislada.
2. Especificar el contexto, los archivos que puede tocar y el criterio de
   aceptacion.
3. Delegar la tarea al subagente `local-worker` con el modelo local mediante
   `opencode run --agent local-worker "<tarea>"` desde `WebDiscoverMerida/`.
4. Revisar los cambios producidos y pedir correcciones si es necesario.
5. Ejecutar las pruebas relevantes antes de continuar.

El subagente no debe abordar varias fases a la vez ni ampliar el alcance sin
autorizacion. Las herramientas que seleccionen `general` o `explore` no
cumplen este flujo y no deben usarse para implementar estas tareas.

## Fase 4: Feature "Descubre Mérida"

### Requisitos de la feature

- La pagina principal conservara el saludo `Hello, World!`.
- Debajo del saludo aparecera un boton o enlace visible con el texto exacto
  `Descubre Mérida`.
- El control llevara a una nueva pagina en `/merida`.
- La nueva pagina tendra HTML semantico, idioma declarado y diseño legible en
  escritorio y movil.
- El contenido sera estatico, en espanol y sin depender de APIs, base de datos
  ni recursos externos.
- La pagina explicara de forma breve que Mérida es una ciudad extremeña y
  describira su relacion historica con los romanos, evitando afirmaciones no
  verificadas o contenido fuera de alcance.
- La pagina incluira un enlace para volver a la pagina principal.

### Tareas pequenas y delegables

Cada tarea se delegara por separado al `local-worker`. El agente principal
revisara el diff y ejecutara los tests indicados antes de aceptar la tarea.

1. **Definir el contenido historico** [x]
   - Archivo permitido: `specs/merida-content.md`.
   - Preparar el texto breve sobre Mérida, Extremadura y su legado romano.
   - Aceptacion: contenido estatico, claro, en espanol y limitado al alcance de
     la feature; no se implementa codigo en esta tarea. Las afirmaciones
     historicas deben revisarse antes de reutilizarse en la plantilla.

2. **Crear la ruta de Mérida** [x]
   - Archivo permitido: `app.py`.
   - Añadir `GET /merida` renderizando una plantilla dedicada.
   - Aceptacion: la ruta existe, no requiere datos externos y conserva el
     comportamiento de `GET /`.

3. **Crear la pagina informativa** [x]
   - Archivo permitido: `templates/merida.html`.
   - Presentar el contenido aprobado con estructura HTML5 semantica, `lang="es"`
     y enlace de vuelta a `/`.
   - Aceptacion: la pagina muestra el contexto extremeño y romano de Mérida de
     forma visible y legible.

4. **Añadir el acceso desde la pagina principal** [x]
   - Archivo permitido: `templates/index.html`.
   - Añadir debajo de `Hello, World!` el control visible `Descubre Mérida` que
     apunte a `/merida`.
   - Aceptacion: el saludo no cambia y el enlace funciona mediante una URL
     generada por Flask.

5. **Adaptar los estilos** [x]
   - Archivos permitidos: `static/styles.css` y, solo si fuera necesario,
     las plantillas de esta feature.
   - Dar estilo consistente al boton, los enlaces y la pagina informativa,
     manteniendo el diseño responsive.
   - Aceptacion: no se añade JavaScript ni dependencias frontend y el contenido
     sigue siendo legible en movil.

6. **Añadir pruebas de la feature** [x]
   - Archivo permitido: `tests/test_app.py` o nuevos tests dentro de `tests/`.
   - Tests requeridos:
     - `GET /` devuelve HTTP 200 y conserva `Hello, World!`.
     - La respuesta de `/` contiene un enlace `Descubre Mérida` hacia `/merida`.
     - `GET /merida` devuelve HTTP 200.
     - La pagina `/merida` contiene el contexto de Mérida, Extremadura y los
       romanos, ademas del enlace de vuelta a `/`.
   - Aceptacion: todos los tests pasan usando Flask test client, sin servidor
     externo.

7. **Actualizar la documentacion** [x]
   - Archivo permitido: `README.md`.
   - Documentar las rutas `/` y `/merida`, el contenido de la nueva pagina y
     los comandos de ejecucion y pruebas.
   - Aceptacion: el README describe el comportamiento real y mantiene las
     instrucciones de delegacion al `local-worker`.

### Orden y verificacion

Las tareas 1 y 2 deben completarse antes de crear la plantilla. La tarea 4
depende de la ruta y la tarea 6 debe ejecutarse despues de terminar las tareas
2 a 5. Tras cada delegacion se usara el siguiente flujo desde `WebDiscoverMerida/`:

```bash
opencode run --agent local-worker "<tarea pequena con archivos y aceptacion>"
```

Despues de cada resultado, el agente principal revisara los archivos permitidos
y ejecutara la prueba relevante. Al final ejecutara:

```bash
.venv/bin/python -m pytest
flask --app app run
```

## Fase 5: Entrega

- [x] Revisar que no haya archivos generados o secretos.
- [x] Confirmar que el README coincide con el comportamiento real.
- [ ] Marcar la version 1.0 como lista.

## Fase 6: Feature "Mérida: qué ver y visitar"

### Objetivo

Ampliar la pagina `/merida` con contenido turistico util para planificar una
visita, combinando imagenes representativas e informacion breve sobre los
principales lugares que ver y visitar en la ciudad.

### Requisitos de la feature

- Mantener la introduccion historica existente y el enlace para volver a `/`.
- Incluir una imagen principal y una imagen por cada lugar destacado, servidas
  desde el propio proyecto sin depender de recursos externos.
- Acompañar cada imagen de un texto alternativo descriptivo y una referencia de
  autoria o licencia cuando corresponda.
- Presentar informacion clara y verificada sobre lugares como el Teatro Romano,
  el Anfiteatro, el Puente Romano, el Acueducto de los Milagros y el Museo
  Nacional de Arte Romano.
- Indicar de forma breve que se debe comprobar horarios, tarifas y condiciones
  de visita antes de acudir, sin inventar datos operativos.
- Organizar el contenido con HTML semantico y un diseño legible en escritorio y
  movil.
- Mantener el contenido estatico, en español y sin añadir JavaScript,
  autenticacion, base de datos ni APIs.

### Tareas pequeñas y delegables

1. **Investigar y aprobar el contenido turistico** [x]
   - Archivo permitido: `specs/merida-visit-content.md`.
   - Documentar una descripcion breve y verificable de cada lugar, junto con la
     fuente consultada y el alcance de la informacion.
   - Aceptacion: el contenido diferencia hechos historicos de recomendaciones y
     no incluye horarios, precios o promesas no verificadas.

2. **Preparar las imagenes locales** [x]
   - Archivos permitidos: `static/images/` y, si fuera necesario,
     `specs/merida-visit-content.md`.
   - Incorporar imagenes optimizadas, con nombres descriptivos y licencia o
     atribucion documentada.
   - Aceptacion: todas las imagenes se cargan desde el proyecto, tienen un
     formato razonable para web y cuentan con texto alternativo previsto.

3. **Ampliar la plantilla de Mérida** [x]
   - Archivo permitido: `templates/merida.html`.
   - Añadir una seccion de lugares destacados con imagen, nombre y descripcion.
   - Aceptacion: la informacion es visible, escaneable y conserva el contenido
     historico ya aprobado.

4. **Adaptar los estilos y la accesibilidad** [x]
   - Archivo permitido: `static/styles.css`.
   - Crear una composicion responsive para la imagen principal y las tarjetas o
     bloques informativos, sin romper la pagina existente.
   - Aceptacion: el contenido se puede leer y recorrer en movil, las imagenes no
     desbordan su contenedor y los enlaces mantienen estados de foco visibles.

5. **Actualizar pruebas y documentacion** [x]
   - Archivos permitidos: `tests/test_app.py` o nuevos tests dentro de `tests/`,
     y `README.md`.
   - Verificar que `/merida` mantiene el contexto historico, incluye los lugares
     destacados, referencia las imagenes y conserva los enlaces de navegacion.
   - Aceptacion: todos los tests pasan con Flask test client y el README describe
     el nuevo contenido y la ubicacion de los recursos.

### Orden y verificacion

Las tareas 1 y 2 deben completarse antes de modificar la plantilla. La tarea 4
se realizara despues de la tarea 3 y la tarea 5 al finalizar las anteriores.
Tras cada tarea se revisara el diff y se ejecutaran las pruebas relevantes. Al
final se ejecutara:

```bash
.venv/bin/python -m pytest
```

## Fuera de alcance

Base de datos, autenticacion, despliegue cloud, internacionalizacion,
persistencia y funcionalidades interactivas.
