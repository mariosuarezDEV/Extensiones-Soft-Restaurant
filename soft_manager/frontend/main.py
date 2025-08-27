from flask import Flask, jsonify
import pymongo
import requests as req

app = Flask(__name__)

cliente = pymongo.MongoClient("mongodb://100.109.93.61:27017/")
db = cliente.mongoffice


@app.route("/")
def home():
    return jsonify({"message": "Hola mundo"}), 200


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
