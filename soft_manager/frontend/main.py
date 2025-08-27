from flask import Flask, jsonify, render_template, request
import pymongo
import requests as req
from datetime import datetime

app = Flask(__name__)

cliente = pymongo.MongoClient("mongodb://100.109.93.61:27017/")
db = cliente.mongoffice
API_URL = "http://127.0.0.1:8000"


@app.route("/")
def home():
    # Obtener la fecha de ayer
    yesterday = datetime.now().replace(day=datetime.now().day - 1)
    # Formatear la fecha en el formato YYYY-MM-DD
    formatted_date = yesterday.strftime("%Y-%m-%d")
    ventas = req.get(f"{API_URL}/ventas?fecha={formatted_date}")
    return render_template("index.html", ventas=ventas.json(), fecha=formatted_date)


@app.route("/mantenimiento", methods=["GET", "POST"])
def mantenimiento():
    if request.method == "GET":
        return render_template("mantenimiento.html")
    if request.method == "POST":
        fecha_inicio = request.form.get("fecha_inicio")
        fecha_fin = request.form.get("fecha_fin")
        sucursal = request.form.get("sucursal")
        return jsonify(
            {"inicio": fecha_inicio, "fin": fecha_fin, "sucursal": sucursal}
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
    app.run(debug=True)
