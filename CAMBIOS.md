# Registro de cambios (contexto para IA)

Resumen de los cambios recientes para que una IA entienda el estado actual del
proyecto sin revisar todo el historial. Agrega las novedades al inicio.
Complementa a `AGENTS.md`.

## 2026-10-28 — Un backend por sucursal con Docker Compose

### Qué hace
`soft_manager/docker-compose.yml` levanta `backend-centro`,
`backend-araucarias` y `backend-anahuac` (misma imagen, distinto `DB_HOST`) y
el `frontend`. El selector de sucursal del frontend ya decide a qué backend se
llama (`SERVIDORES` en `frontend/main.py`); no hay que editar IPs.

### Cambios
- `backend/backend/settings.py`: `DATABASES` lee `DB_HOST`, `DB_PORT`,
  `DB_NAME`, `DB_USER`, `DB_PASSWORD` (defaults = valores anteriores).
- `Dockerfile`: copia `openssl_legacy.cnf` y fija `OPENSSL_CONF`.
- Nuevo `Dockerfile.frontend`, `docker-compose.yml` y `.env.example`;
  `.dockerignore` ya no excluye `frontend`.
- `frontend/main.py`: `SERVIDORES` lee `BACKEND_<SUCURSAL>`, Mongo lee
  `MONGO_URI`, y `/backup/<folio>` acepta `?sucursal=`.

- Servicio `mongo` (`mongo:7`, volumen `mongo_data`, publicado en `0.0.0.0:27018` con `--auth`; requiere
  `MONGO_USER`/`MONGO_PASSWORD` en `.env`) que
  usa el frontend (URI con usuario/contraseña por defecto).

- Solo `backend-araucarias` publica `127.0.0.1:8000`; los otros backends no.

### Uso
Requiere Tailscale activo en el equipo que corre Docker. Desde `soft_manager/`:
copia `.env.example` a `.env`, completa las IPs Tailscale y ejecuta
`docker compose up --build`; el frontend queda en http://localhost:5000.
Sin Docker todo funciona como antes (defaults a `localhost`).

## 2026-10-12 — Productos por sucursal (rama `dinamicproducts`)

### Qué hace
El ajuste de ventas (`POST /ventas/ajuste/<folio>`) elige la lista de
productos según la sucursal, que llega como query param `?sucursal=...`:

- `anahuac` → `backend/ventas/scripts.py`
- cualquier otra (`centro`, `araucarias`, `desarrollo` o sin parámetro) →
  `backend/ventas/prodsuc.py` (nuevo, antes sin versionar)

### Cambios
- El selector es `fuente_productos(sucursal)` en `backend/ventas/views.py`;
  ignora mayúsculas y espacios. Ambos módulos exponen `get_sustituno()`.
- El frontend (`frontend/main.py`) envía la sucursal del formulario en el POST
  de ajuste: `req.post(url, params={"sucursal": sucursal})`.
- `mant_express.py` no envía sucursal, así que ahora usa `prodsuc.py` por
  defecto (antes usaba `scripts.py`).

### Pruebas
- `backend/ventas/tests.py`: pruebas del selector con `SimpleTestCase`, sin
  base de datos (`uv run python manage.py test ventas`).
- `frontend/test_mantenimiento.py`: las llamadas esperadas al POST de ajuste
  ahora incluyen `params={"sucursal": ...}` y se agregó `historial` a la
  respuesta esperada (esa expectativa faltaba desde la rama `anahuac`).

## 2026-10-02 — Historial de mantenimientos (rama `anahuac`)

Commits: `29c63df`, `2b0b1f8`, `f936b5a`.

### Qué hace
Al terminar el POST de `/mantenimiento` (`soft_manager/frontend/main.py`), se
envía un POST a `{HISTORIAL_API_URL}/historial_mantenimientos` **por cada fecha
del rango seleccionado** (todas, tengan ventas o no). Se hace después de
procesar todas las ventas, para que los días sin ventas (`continue`) también se
registren.

Payload:

```json
{
  "id_sucursal": 3,
  "fecha_aplicacion": "2026-10-02",
  "fecha_mantenimiento": "2026-09-29"
}
```

- `fecha_aplicacion`: día en que se ejecuta el mantenimiento (`date.today()`).
- `fecha_mantenimiento`: la fecha de ese día del rango.
- La respuesta JSON de `/mantenimiento` incluye `historial`: lista con un
  resultado por fecha (`fecha`, `enviado`, `motivo` si falló, `payload`).
- Un fallo del historial **no** rompe el mantenimiento; solo se informa.
- Si falta la URL o la sucursal no tiene id, se devuelve un solo resultado sin
  repetirlo por cada día.

### Ids de sucursal (`ID_SUCURSAL`)
`centro` = 1, `araucarias` = 2, `anahuac` = 3. `desarrollo` no envía nada.

### Configuración
- `HISTORIAL_API_URL` se lee de `soft_manager/frontend/.env` con `python-dotenv`
  (`load_dotenv` con ruta relativa a `main.py`, no depende del directorio de
  ejecución). El `.env` no se versiona.
- `_normalizar_url` quita espacios, comillas y `/` final, y agrega `http://` si
  falta el esquema.
- La variable se lee solo al arrancar: hay que reiniciar Flask tras cambiarla.
- Errores típicos en `historial[].motivo`:
  - `HISTORIAL_API_URL no configurada`: falta la variable o el `.env`.
  - `No connection adapters were found ...`: la URL no tenía `http://`
    (resuelto por `_normalizar_url`).

### Otros cambios en la rama
- Opción "Anahuac" en el selector (`templates/mantenimiento.html`) y en
  `SERVIDORES`.
- MongoDB en `mongodb://localhost:27017/`.
- `backend/backend/asgi.py` usa `backend.settings`.
- Nuevos `Dockerfile`, `DockerfileIA` y `.dockerignore`.
- Dependencia `python-dotenv` en `pyproject.toml` y `uv.lock`.

### Ojo
- `SERVIDORES` apunta todo a `localhost` en esta rama; ajusta las IPs según el
  servidor donde corra.
- No ejecutes `/mantenimiento` contra servidores reales para probar: modifica
  ventas.
