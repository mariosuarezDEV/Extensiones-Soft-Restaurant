# Guía del proyecto

## Alcance y estructura

Estas instrucciones aplican a todo el repositorio.

- El proyecto Python está en `soft_manager/`, con Python 3.13 y dependencias
  gestionadas por `uv`.
- `soft_manager/backend/` contiene Django, Django REST Framework y la API de
  ventas. La configuración está en `backend/settings.py` dentro de esa carpeta.
- `soft_manager/backend/ventas/` contiene modelos del esquema de Soft Restaurant,
  serializadores, rutas, vistas y selección de productos en `scripts.py`.
- `soft_manager/frontend/main.py` contiene la aplicación Flask y su integración
  con Django y MongoDB. Sus plantillas están en `frontend/templates/`.
- `soft_manager/mant_express.py` ejecuta operaciones de mantenimiento.
- Consulta `README.md` para instalar herramientas y configurar las conexiones.

## Comandos de desarrollo

Sincroniza desde `soft_manager/`:

```console
uv sync
```

Desde `soft_manager/backend/`:

```console
uv run python manage.py check
uv run python manage.py runserver 0.0.0.0:8000
```

Desde `soft_manager/frontend/`:

```console
uv run flask --app main.py routes
uv run flask --app main.py run
```

Django y Flask se ejecutan en terminales separadas y comparten `.venv`.
Agrega dependencias con `uv add` desde `soft_manager/` y versiona tanto
`pyproject.toml` como `uv.lock`.

## Convenciones

- Conserva la organización y el estilo del archivo que edites; evita reformateos
  o refactorizaciones ajenos a la tarea.
- Mantén en español la documentación del proyecto.
- Conserva los nombres de tablas y columnas del esquema externo y los contratos
  de rutas/respuestas, salvo que la tarea requiera cambiarlos.
- Los modelos con `managed = False` representan tablas existentes. No cambies
  esa opción ni generes cambios de esquema como parte de una instalación local.
- No agregues credenciales, datos de ventas reales ni archivos `.env`.
  Las conexiones actuales se configuran en el código; no supongas que se carga
  automáticamente un archivo `.env`.

## Validación y datos

- Ejecuta las comprobaciones de Django y de rutas Flask cuando corresponda al
  cambio. Informa cuáles se ejecutaron y cualquier dependencia faltante.
- `backend/ventas/tests.py` es un esqueleto sin pruebas. Para cambios de lógica,
  usa pruebas enfocadas con datos sintéticos y servicios aislados.
- No uses `mant_express.py`, el POST de `/mantenimiento` o
  `/ventas/ajuste/<folio>` como pruebas contra bases reales: modifican ventas.
  Valida esas operaciones en una base de desarrollo preparada para ello.
- No subas archivos CSV, aunque estén dentro de otra carpeta o tengan la
  extensión en mayúsculas. Si están versionados, retíralos con
  `git rm --cached` conservando los archivos locales.
- Antes de un commit, revisa `git diff --check`, `git diff --cached --stat` y
  `git status --short`. Conserva los cambios del usuario y agrega únicamente
  archivos relacionados con la tarea.
