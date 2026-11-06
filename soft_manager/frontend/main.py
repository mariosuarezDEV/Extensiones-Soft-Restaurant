from flask import Flask, jsonify, redirect, render_template, request
from datetime import datetime

from servicio import SERVIDORES, db, req
from tareas import celery_app, ejecutar_mantenimiento
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/mantenimiento")


@app.route("/mantenimiento", methods=["GET", "POST"])
def mantenimiento():
    if request.method == "GET":
        return render_template("mantenimiento.html")

    # Datos del formulario (una o varias sucursales)
    fecha_inicio = request.form.get("fecha_inicio")
    fecha_fin = request.form.get("fecha_fin")
    sucursales = request.form.getlist("sucursal")

    try:
        inicio = datetime.strptime(fecha_inicio or "", "%Y-%m-%d").date()
        fin = datetime.strptime(fecha_fin or "", "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Fechas invalidas (use AAAA-MM-DD)"}), 400
    if fin < inicio:
        return jsonify({"error": "La fecha fin es anterior a la fecha inicio"}), 400
    if not sucursales or any(s not in SERVIDORES for s in sucursales):
        return jsonify({"error": "Seleccione una o mas sucursales validas"}), 400

    # Un trabajo independiente por sucursal; la peticion responde de inmediato
    tareas = []
    for sucursal in dict.fromkeys(sucursales):
        tarea = ejecutar_mantenimiento.delay(
            sucursal, inicio.isoformat(), fin.isoformat()
        )
        tareas.append({"sucursal": sucursal, "id": tarea.id})
    return jsonify({"tareas": tareas}), 202


@app.route("/mantenimiento/estado/<id_tarea>", methods=["GET"])
def estado_mantenimiento(id_tarea):
    tarea = celery_app.AsyncResult(id_tarea)
    estado = tarea.state
    respuesta = {"estado": estado}
    if estado == "PROGRESS":
        respuesta["progreso"] = tarea.info
    elif estado == "SUCCESS":
        respuesta["resultado"] = tarea.result
    elif estado == "FAILURE":
        respuesta["error"] = str(tarea.result)
    return jsonify(respuesta), 200


@app.route("/stats", methods=["GET"])
def listar_ventas():
    ventas = db.ventas.find({}, {"_id": 0})  # excluir el campo _id
    ventas = list(ventas)
    return jsonify({"Ventas Almacenadas": len(ventas)}), 200


@app.route("/backup/<int:folio>", methods=["GET"])
def guardar_venta(folio):
    sucursal = request.args.get("sucursal", "desarrollo")
    ip_server = SERVIDORES.get(sucursal, SERVIDORES["desarrollo"])
    venta = req.get(f"http://{ip_server}:8000/ventas/{folio}")
    venta = venta.json()
    try:
        db.ventas.insert_one(venta)
        return jsonify({"message": f"La venta con folio {folio} fue guardada"}), 200
    except Exception:
        return jsonify({"message": f"Error al guardar la venta con folio {folio}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("FRONTEND_PORT", "6001")), debug=True)
