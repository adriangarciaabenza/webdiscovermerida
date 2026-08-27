# Constitucion de WebDiscoverMerida

**Version:** 1.1  
**Estado:** propuesta inicial

## Mision

Construir la aplicacion mas pequena que demuestre de forma clara y fiable una
pagina web funcional con el mensaje `Hello, World!`.

## Principios

### 1. Alcance minimo

No se anadiran funcionalidades, dependencias o infraestructura que no sean
necesarias para mostrar el mensaje y servir la pagina localmente.

### 2. Claridad antes que abstraccion

El codigo debe ser legible para una persona que empieza. Se evitaran capas,
patrones y configuracion innecesarios.

### 3. Ejecucion reproducible

Las instrucciones de instalacion y arranque deben funcionar desde un entorno
limpio y quedar documentadas en el README.

### 4. Calidad verificable

Antes de considerar terminada una entrega se comprobara que la aplicacion
arranca, responde con HTTP 200 y muestra exactamente `Hello, World!`.

### 5. Accesibilidad basica

La pagina usara HTML semantico, un idioma declarado y una estructura visible y
legible tanto en escritorio como en movil.

### 6. Delegacion en tareas pequenas

Durante la implementacion, el agente principal descompondra el trabajo en
tareas pequenas, independientes y verificables. Cada tarea se delegara al
subagente `local-worker`, que usara el modelo local configurado en OpenCode.
La delegacion se realizara invocando `opencode run --agent local-worker
"<tarea>"` desde el directorio del proyecto; no se sustituira por los
subagentes genericos `general` o `explore`. El agente principal revisara el
resultado y ejecutara las pruebas relevantes antes de aceptar la tarea o pasar
a la siguiente.

## Criterios de aceptacion constitucionales

- Una persona nueva puede arrancar el proyecto siguiendo el README.
- La pagina principal muestra `Hello, World!` sin requerir datos externos.
- No existen secretos, credenciales ni servicios externos necesarios.
- Las decisiones tecnicas permanecen alineadas con `tech-stack.md`.
- Cada tarea delegada tiene un objetivo y un criterio de aceptacion claros.
- Ningun cambio del subagente se integra sin revision y verificacion.
