# Stack tecnologico

## Decisiones

| Area | Eleccion | Motivo |
| --- | --- | --- |
| Lenguaje | Python 3.12+ | Sencillo y disponible para una demo minima |
| Servidor web | Flask 3.x | Arranque directo con poca configuracion |
| Plantillas | Jinja2 incluida con Flask | Permite separar HTML de la logica |
| Presentacion | HTML5 y CSS3 | Sin build ni dependencias de frontend |
| Pruebas | pytest y Flask test client | Verificacion rapida sin levantar un proceso externo |
| Dependencias | `requirements.txt` | Instalacion reproducible |

## Estructura prevista

```text
HelloWorld2/
  app.py
  requirements.txt
  README.md
  templates/
    index.html
  static/
    styles.css
  tests/
    test_app.py
  specs/
```

## Restricciones

- No se usara JavaScript para la funcionalidad inicial.
- No se incorporara una base de datos, API externa o sistema de usuarios.
- La aplicacion se ejecutara con `flask --app app run`.
- Las versiones concretas instaladas se fijaran en `requirements.txt`.
