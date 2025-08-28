from flask import Flask, jsonify, render_template, request
import pymongo
import requests as req
from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__)

cliente = pymongo.MongoClient("mongodb://100.109.93.61:27017/")
db = cliente.mongoffice

SERVIDORES = {
    "centro": "26.61.16.123",
    "araucarias": "26.217.212.35",
    "desarrollo": "26.114.158.30",
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/mantenimiento", methods=["GET", "POST"])
def mantenimiento():
    if request.method == "GET":
        return render_template("mantenimiento.html")
    if request.method == "POST":
        # Datos del formulario
        fecha_inicio = request.form.get("fecha_inicio")
        fecha_fin = request.form.get("fecha_fin")
        sucursal = request.form.get("sucursal")

        ip_server = SERVIDORES.get(sucursal)
        API_URL = f"http://{ip_server}:8000"

        # Nombre del mes actual
        mes_actual = datetime.now().strftime("%m")
        # Nombre de la coleccion
        colecion = f"{mes_actual}_{sucursal}"

        # Obtener todas las fechas entre fecha_inicio y fecha_fin
        fechas = []
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
        fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
        delta = fin - inicio
        for i in range(delta.days + 1):
            dia = inicio + timedelta(days=i)
            print(dia)
            fechas.append(dia)

        # Obtener ventas por cada fecha
        for fecha in fechas:
            ventas = req.get(f"{API_URL}/ventas?fecha={fecha}")
            ventas = ventas.json()
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
                # Obtener folio de la venta
                folio = venta["folio"]
                # Obtener informacion del folio
                venta_detalle = req.get(f"{API_URL}/ventas/{folio}")
                venta_detalle = venta_detalle.json()
                try:
                    # Insertar en la coleccion correspondiente
                    db[colecion].insert_one(venta_detalle)
                    # TODO Traer el enpoint para aplicar mantenimiento a la venta
                    # Validar si el folio actual este en el dataframe filtrado
                    if folio in ventas_filtradas["folio"].values:
                        # Aplicar mantenimiento a la venta
                        ajuste = req.post(f"{API_URL}/ventas/ajuste/{folio}")
                        if ajuste.status_code == 200:
                            print(f"Venta con folio {folio} ajustada")
                        else:
                            print(f"Error al ajustar la venta con folio {folio}")
                except Exception as e:
                    print(f"Error al guardar la venta con folio {folio}: {e}")

        return jsonify(
            {
                "inicio": fecha_inicio,
                "fin": fecha_fin,
                "sucursal": sucursal,
                "total_ventas": len(ventas),
            }
        ), 200


@app.route("/stats", methods=["GET"])
def listar_ventas():
    ventas = db.ventas.find({}, {"_id": 0})  # excluir el campo _id
    ventas = list(ventas)
    return jsonify({"Ventas Almacenadas": len(ventas)}), 200


@app.route("/backup/<int:folio>", methods=["GET"])
def guardar_venta(folio):
    venta = req.get(f"http://127.0.0.1:8000/ventas/{folio}")
    venta = venta.json()
    try:
        db.ventas.insert_one(venta)
        return jsonify({"message": f"La venta con folio {folio} fue guardada"}), 200
    except Exception:
        return jsonify({"message": f"Error al guardar la venta con folio {folio}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
