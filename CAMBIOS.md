# Registro de cambios (contexto para IA)

Resumen de los cambios recientes para que una IA entienda el estado actual del
proyecto sin revisar todo el historial. Agrega las novedades al inicio.
Complementa a `AGENTS.md`.

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
