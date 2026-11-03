import unittest
from contextlib import redirect_stdout
from datetime import date, timedelta
from io import StringIO
from unittest.mock import Mock, call, patch


class MantenimientoTests(unittest.TestCase):
    def setUp(self):
        import main, servicio, tareas

        self.main, self.servicio, self.tareas = main, servicio, tareas
        self.main.app.config["TESTING"] = True
        self.client = self.main.app.test_client()

    def test_procesa_el_rango_omitiendo_dias_sin_ventas(self):
        escenarios = {
            "primer_dia_vacio": (False, True),
            "dia_intermedio_vacio": (True, False, True),
            "ultimo_dia_vacio": (True, False),
            "dias_vacios_consecutivos": (True, False, False, True),
            "todos_vacios": (False, False, False),
            "un_dia_vacio": (False,),
            "un_dia_con_ventas": (True,),
            "todos_con_ventas": (True, True),
        }
        for nombre, dias_con_ventas in escenarios.items():
            with self.subTest(escenario=nombre):
                inicio = date(2026, 1, 1)
                fin = inicio + timedelta(days=len(dias_con_ventas) - 1)
                respuestas = {}
                consultas = []
                ajustes = []
                respaldos = []
                for indice, hay_ventas in enumerate(dias_con_ventas):
                    fecha = inicio + timedelta(days=indice)
                    url = f"http://localhost:8000/ventas?fecha={fecha}"
                    consultas.append(call(url))
                    respuestas[url] = []
                    if hay_ventas:
                        folio = indice + 1
                        venta = {
                            "folio": folio,
                            "efectivo": "200.00",
                            "tarjeta": "0.00",
                            "otros": "0.00",
                            "facturado": False,
                            "mesa": "1",
                        }
                        detalle = {
                            "Venta": venta,
                            "Consumo": [],
                            "Pago": [],
                            "Factura": None,
                        }
                        respuestas[url] = [venta]
                        url_detalle = f"http://localhost:8000/ventas/{folio}"
                        respuestas[url_detalle] = detalle
                        consultas.append(call(url_detalle))
                        respaldos.append(call(detalle))
                        ajustes.append(
                            call(
                                f"http://localhost:8000/ventas/ajuste/{folio}",
                                params={"sucursal": "desarrollo"},
                            )
                        )

                with (
                    patch.object(self.servicio, "db") as db,
                    patch.object(self.tareas.req, "get") as get,
                    patch.object(self.tareas.req, "post") as post,
                    patch.object(self.tareas.pd.DataFrame, "to_csv") as to_csv,
                    redirect_stdout(StringIO()),
                ):
                    get.side_effect = lambda url: Mock(
                        json=Mock(return_value=respuestas[url])
                    )
                    post.return_value.status_code = 200
                    avances = []
                    resultado = self.tareas.procesar_mantenimiento(
                        "desarrollo",
                        inicio.isoformat(),
                        fin.isoformat(),
                        lambda *args: avances.append(args),
                    )

                self.assertEqual(
                    resultado,
                    {
                        "inicio": inicio.isoformat(),
                        "fin": fin.isoformat(),
                        "sucursal": "desarrollo",
                        "total_ventas": sum(dias_con_ventas),
                        "historial": [
                            {
                                "fecha": inicio.isoformat(),
                                "enviado": False,
                                "motivo": "sucursal sin id en la API",
                            }
                        ],
                    },
                )
                self.assertEqual(
                    [a[:2] for a in avances],
                    [(i + 1, len(dias_con_ventas)) for i in range(len(dias_con_ventas))],
                )
                self.assertEqual(get.call_args_list, consultas)
                self.assertEqual(post.call_args_list, ajustes)
                self.assertEqual(
                    db.__getitem__.return_value.insert_one.call_args_list, respaldos
                )
                self.assertEqual(to_csv.call_count, sum(dias_con_ventas))

    def test_post_encola_una_tarea_por_sucursal(self):
        with patch.object(self.main.ejecutar_mantenimiento, "delay") as delay:
            delay.side_effect = [Mock(id="a"), Mock(id="b")]
            respuesta = self.client.post(
                "/mantenimiento",
                data={
                    "fecha_inicio": "2026-01-01",
                    "fecha_fin": "2026-01-02",
                    "sucursal": ["centro", "anahuac"],
                },
            )
        self.assertEqual(respuesta.status_code, 202)
        self.assertEqual(
            respuesta.get_json(),
            {
                "tareas": [
                    {"sucursal": "centro", "id": "a"},
                    {"sucursal": "anahuac", "id": "b"},
                ]
            },
        )
        self.assertEqual(
            delay.call_args_list,
            [
                call("centro", "2026-01-01", "2026-01-02"),
                call("anahuac", "2026-01-01", "2026-01-02"),
            ],
        )

    def test_post_rechaza_datos_invalidos(self):
        casos = [
            {"fecha_inicio": "x", "fecha_fin": "2026-01-02", "sucursal": "centro"},
            {"fecha_inicio": "2026-01-03", "fecha_fin": "2026-01-02", "sucursal": "centro"},
            {"fecha_inicio": "2026-01-01", "fecha_fin": "2026-01-02"},
            {"fecha_inicio": "2026-01-01", "fecha_fin": "2026-01-02", "sucursal": "otra"},
        ]
        with patch.object(self.main.ejecutar_mantenimiento, "delay") as delay:
            for datos in casos:
                with self.subTest(datos=datos):
                    self.assertEqual(
                        self.client.post("/mantenimiento", data=datos).status_code, 400
                    )
            delay.assert_not_called()

    def test_estado_de_la_tarea(self):
        escenarios = {
            "PENDING": ({}, {"estado": "PENDING"}),
            "PROGRESS": ({"info": {"actual": 1}}, {"estado": "PROGRESS", "progreso": {"actual": 1}}),
            "SUCCESS": ({"result": {"total_ventas": 3}}, {"estado": "SUCCESS", "resultado": {"total_ventas": 3}}),
            "FAILURE": ({"result": ValueError("boom")}, {"estado": "FAILURE", "error": "boom"}),
        }
        for estado, (atributos, esperado) in escenarios.items():
            with self.subTest(estado=estado):
                resultado = Mock(state=estado, **atributos)
                with patch.object(
                    self.main.celery_app, "AsyncResult", return_value=resultado
                ):
                    respuesta = self.client.get("/mantenimiento/estado/abc")
                self.assertEqual(respuesta.get_json(), esperado)


if __name__ == "__main__":
    unittest.main()
