# Extensiones Soft Restaurant

Herramientas para consultar y gestionar ventas de Soft Restaurant. El backend usa
Django y Django REST Framework con SQL Server; la interfaz usa Flask y guarda
respaldos de ventas en MongoDB.

## Estructura

```text
.
├── AGENTS.md                       # Guía de trabajo para agentes
└── soft_manager/
    ├── pyproject.toml              # Dependencias de ambos servidores
    ├── uv.lock                     # Versiones de dependencias
    ├── .python-version             # Python 3.13
    ├── backend/
    │   ├── manage.py
    │   ├── backend/settings.py     # Configuración de Django y SQL Server
    │   └── ventas/                 # Modelos, API y lógica de ventas
    ├── frontend/
    │   ├── main.py                 # Aplicación Flask
    │   └── templates/
    └── mant_express.py             # Script de mantenimiento de ventas
```

## Requisitos

- Git y `uv`.
- Python 3.13, instalable con `uv` como se indica abajo.
- Acceso a una base de SQL Server con el esquema de Soft Restaurant.
- [Microsoft ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).
  Este controlador se instala en el sistema; `uv sync` no lo instala.
- Acceso a MongoDB para respaldos y estadísticas.

## Instalar uv

En Windows, desde PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

En macOS o Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Abre otra terminal después de instalarlo y comprueba:

```console
uv --version
```

Referencia: [instalación oficial de uv](https://docs.astral.sh/uv/getting-started/installation/).

## Clonar y sincronizar el proyecto

```console
git clone --branch Dev https://github.com/mariosuarezDEV/Extensiones-Soft-Restaurant.git
cd Extensiones-Soft-Restaurant/soft_manager
uv python install 3.13
uv sync
```

Si ya tienes el repositorio, entra directamente a `soft_manager` y ejecuta
`uv sync`. Esta es la carpeta que contiene `pyproject.toml` y `uv.lock`;
ambas aplicaciones comparten el entorno `soft_manager/.venv`.

Después de obtener cambios de dependencias, ejecuta nuevamente `uv sync`.
Para exigir que el archivo de bloqueo esté actualizado sin modificarlo, usa
`uv sync --locked`. Mantén `uv.lock` en Git. Consulta la
[guía de proyectos de uv](https://docs.astral.sh/uv/guides/projects/).

## Configurar las conexiones

Antes de usar las funciones que consultan o modifican datos, revisa:

| Archivo | Configuración |
| --- | --- |
| `soft_manager/backend/backend/settings.py` | `DATABASES["default"]`: servidor, puerto, base, usuario, contraseña y controlador ODBC de SQL Server. |
| `soft_manager/frontend/main.py` | `MongoClient(...)`: conexión a MongoDB; `db`: base utilizada para respaldos. |
| `soft_manager/frontend/main.py` | `SERVIDORES`: servidor Django de cada sucursal. Las peticiones usan el puerto 8000. |

Solicita al responsable del entorno los datos de conexión. Actualmente estas
conexiones están definidas en el código; crear un archivo `.env` por sí solo no
las configura, porque el proyecto no carga esas variables.

Los modelos de ventas utilizan tablas existentes con `managed = False`.
`migrate` no crea el esquema de Soft Restaurant. Usa una copia de desarrollo:
el mantenimiento de Flask, el endpoint de ajuste y `mant_express.py` modifican
registros de ventas.

## Ejecutar Django

En una terminal, desde la raíz del repositorio:

```console
cd soft_manager/backend
uv run python manage.py runserver 0.0.0.0:8000
```

Abre [http://127.0.0.1:8000/ventas/?fecha=2026-09-01](http://127.0.0.1:8000/ventas/?fecha=2026-09-01)
y cambia la fecha por una que tenga ventas en tu base.
`0.0.0.0` permite escuchar en todas las interfaces; desde otro equipo usa la IP
del servidor y el puerto 8000.

## Ejecutar Flask

En otra terminal, también desde la raíz del repositorio:

```console
cd soft_manager/frontend
uv run flask --app main.py run
```

Abre [http://127.0.0.1:5000](http://127.0.0.1:5000). Mantén Django ejecutándose
para las funciones que llaman a la API. Detén cada servidor con `Ctrl+C`.

`uv run` utiliza el entorno del proyecto sin activarlo manualmente. Si prefieres
usar los comandos directamente, activa el entorno en cada terminal desde
`soft_manager`:

```powershell
# Windows / PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Después, ejecuta `python manage.py runserver 0.0.0.0:8000` desde `backend`,
o `flask --app main.py run` desde `frontend`.

Estos son servidores de desarrollo. Referencias:
[runserver de Django](https://docs.djangoproject.com/en/5.2/ref/django-admin/#runserver)
y [ejecución de Flask](https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application).

## API de ventas

Las rutas se definen en `soft_manager/backend/ventas/urls.py`.

| Método | Ruta | Función |
| --- | --- | --- |
| GET | `/ventas/?fecha=YYYY-MM-DD` | Listar ventas de una fecha; sin `fecha` devuelve 400. |
| GET | `/ventas/<folio>` | Consultar venta, consumo, pagos y factura, si existe. |
| GET | `/ventas/auditoria/<folio>` | Consultar por número de cheque (`numcheque`). |
| GET | `/ventas/actuales/` | Consultar cheques temporales de la fecha calculada por el servidor. |
| GET | `/ventas/producto/<idproducto>` | Buscar un producto. |
| GET | `/ventas/grupos/` | Listar grupos. |
| POST | `/ventas/ajuste/<folio>` | Modificar una venta con el producto y la cantidad seleccionados por la lógica de ajuste. |

El listado devuelve un arreglo de ventas. El detalle devuelve las claves
`Venta`, `Consumo`, `Pago` y `Factura`.
La configuración de Redis está comentada y las vistas actuales no implementan
la caché de 24 horas descrita en versiones anteriores de esta guía.

## Verificación rápida

Desde `soft_manager/backend`:

```console
uv run python manage.py check
```

Desde `soft_manager/frontend`:

```console
uv run flask --app main.py routes
```

Estas comprobaciones validan la configuración de Django y la carga de rutas de
Flask; no comprueban la conectividad ni el funcionamiento con las bases de datos.
`backend/ventas/tests.py` todavía no contiene pruebas implementadas.

## Archivos locales y Git

El `.gitignore` excluye CSV (incluyendo extensiones en mayúsculas), entornos
virtuales, archivos `.env`, cachés, logs y otros archivos generados por Python.

Los CSV ya versionados se retiran del índice de Git y se conservan localmente.
Esto los elimina de la versión actual del repositorio, pero no del historial
de commits anteriores. No fuerces su incorporación con `git add -f`.
