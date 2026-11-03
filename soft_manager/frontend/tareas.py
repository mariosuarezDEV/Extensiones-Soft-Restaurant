"""Tareas en segundo plano (Celery) para los mantenimientos de ventas."""
import os
from datetime import datetime, timedelta

import pandas as pd
from celery import Celery

import servicio
from servicio import req, registrar_historial

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("soft_manager", broker=REDIS_URL, backend=REDIS_URL)
celery_app.conf.update(
    task_track_started=True,
    result_expires=60 * 60 * 24 * 3,  # los resultados se conservan 3 dias
)


def procesar_mantenimiento(sucursal, fecha_inicio, fecha_fin, progreso=None):
    """Respalda y ajusta las ventas de una sucursal en un rango de fechas.

    `progreso(actual, total, dia, total_ventas)` se llama al terminar cada dia.
    Devuelve el mismo resumen que antes entregaba la vista.
    """
    db = servicio.db
    ip_server = servicio.SERVIDORES.get(sucursal)
    API_URL = f"http://{ip_server}:8000"

    # Nombre de la coleccion: mes actual + sucursal
    colecion = f"{datetime.now().strftime('%m')}_{sucursal}"

    # Obtener todas las fechas entre fecha_inicio y fecha_fin
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    fechas = [inicio + timedelta(days=i) for i in range((fin - inicio).days + 1)]

    # Obtener ventas por cada fecha
    total_ventas = 0
    for indice, fecha in enumerate(fechas, start=1):
        ventas = req.get(f"{API_URL}/ventas?fecha={fecha}")
        ventas = ventas.json()
        if ventas == []:
            print(f"No hay ventas para {fecha}; se omite este dia.")
        else:
            total_ventas += len(ventas)
            # Pasar a un dataframe
            ventas_df = pd.DataFrame(ventas)
            # Convertir los tipos de datos
            ventas_df["efectivo"] = ventas_df["efectivo"].astype(float)
            ventas_df["tarjeta"] = ventas_df["tarjeta"].astype(float)
            ventas_df["otros"] = ventas_df["otros"].astype(float)
            ventas_df["facturado"] = ventas_df["facturado"].astype(str)
            # Obtener solo lo que efectivo > 130 - tarjeta = 0, otros= 0 y mesa nombre diferente a ""
            ventas_filtradas = ventas_df[
                (ventas_df["efectivo"] > 130)  # El cafe vale $129
                & (ventas_df["tarjeta"] == 0)
                & (ventas_df["otros"] == 0)
                & (ventas_df["mesa"] != "")  # Delivery
                & (ventas_df["facturado"] == "False")  # No facturado
            ]
            # Guardar el dataframe filtrado en un archivo csv
            ventas_filtradas.to_csv(f"ventas_filtradas_{fecha}.csv", index=False)

            # Obtener el detalle de cada venta
            for venta in ventas:
                folio = venta["folio"]
                venta_detalle = req.get(f"{API_URL}/ventas/{folio}")
                venta_detalle = venta_detalle.json()
                try:
                    # Insertar en la coleccion correspondiente
                    db[colecion].insert_one(venta_detalle)
                    # Validar si el folio actual este en el dataframe filtrado
                    if folio in ventas_filtradas["folio"].values:
                        # Aplicar mantenimiento a la venta
                        ajuste = req.post(
                            f"{API_URL}/ventas/ajuste/{folio}",
                            params={"sucursal": sucursal},
                        )
                        if ajuste.status_code == 200:
                            print(f"Venta con folio {folio} ajustada")
                        else:
                            print(f"Error al ajustar la venta con folio {folio}")
                except Exception as e:
                    print(f"Error al guardar la venta con folio {folio}: {e}")

        if progreso:
            progreso(indice, len(fechas), fecha.isoformat(), total_ventas)

    # Registrar en el historial cada fecha del rango
    historial = []
    for fecha in fechas:
        resultado = registrar_historial(sucursal, fecha)
        historial.append({"fecha": fecha.isoformat(), **resultado})
        # Si no se puede enviar por configuracion, no repetir el mismo error
        if not resultado["enviado"] and "payload" not in resultado:
            break

    return {
        "inicio": fecha_inicio,
        "fin": fecha_fin,
        "sucursal": sucursal,
        "total_ventas": total_ventas,
        "historial": historial,
    }


@celery_app.task(bind=True, name="mantenimiento.ejecutar")
def ejecutar_mantenimiento(self, sucursal, fecha_inicio, fecha_fin):
    def progreso(actual, total, dia, total_ventas):
        self.update_state(
            state="PROGRESS",
            meta={
                "actual": actual,
                "total": total,
                "dia": dia,
                "total_ventas": total_ventas,
            },
        )

    return procesar_mantenimiento(sucursal, fecha_inicio, fecha_fin, progreso)
