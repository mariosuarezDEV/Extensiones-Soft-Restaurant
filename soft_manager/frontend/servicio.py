"""Configuracion y utilidades compartidas por Flask (main.py) y Celery (tareas.py)."""
import pymongo
import requests as req
import os
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

# .env en la raiz del frontend (independiente del directorio de ejecucion)
load_dotenv(Path(__file__).parent / ".env")

cliente = pymongo.MongoClient(
    os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
)
db = cliente.mongoffice

SERVIDORES = {
    # En Docker Compose cada variable apunta al servicio de esa sucursal
    "centro": os.environ.get("BACKEND_CENTRO", "localhost"),
    "araucarias": os.environ.get("BACKEND_ARAUCARIAS", "localhost"),
    "anahuac": os.environ.get("BACKEND_ANAHUAC", "localhost"),
    "desarrollo": os.environ.get("BACKEND_DESARROLLO", "localhost"),
}

# IDs de sucursal en la API de historial ("desarrollo" no se reporta)
ID_SUCURSAL = {"centro": 1, "araucarias": 2, "anahuac": 3}

def _normalizar_url(valor):
    """Quita comillas/espacios/slash final y agrega http:// si falta el esquema."""
    valor = valor.strip().strip("'\"").rstrip("/")
    if valor and "://" not in valor:
        valor = f"http://{valor}"
    return valor


HISTORIAL_API_URL = _normalizar_url(os.environ.get("HISTORIAL_API_URL", ""))


def registrar_historial(sucursal, fecha_mantenimiento):
    """Envia el registro del mantenimiento a la API de historial.

    Nunca lanza excepciones: devuelve un dict con el resultado.
    """
    id_sucursal = ID_SUCURSAL.get(sucursal)
    if id_sucursal is None:
        return {"enviado": False, "motivo": "sucursal sin id en la API"}
    if not HISTORIAL_API_URL:
        return {"enviado": False, "motivo": "HISTORIAL_API_URL no configurada"}

    payload = {
        "id_sucursal": id_sucursal,
        "fecha_aplicacion": date.today().isoformat(),
        "fecha_mantenimiento": fecha_mantenimiento.isoformat(),
    }
    try:
        resp = req.post(
            f"{HISTORIAL_API_URL}/historial_mantenimientos", json=payload, timeout=10
        )
        if resp.ok:
            return {"enviado": True, "payload": payload}
        return {
            "enviado": False,
            "motivo": f"HTTP {resp.status_code}",
            "payload": payload,
        }
    except req.RequestException as e:
        return {"enviado": False, "motivo": str(e), "payload": payload}
