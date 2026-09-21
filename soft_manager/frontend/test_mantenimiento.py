import importlib.util
import unittest
from contextlib import redirect_stdout
from datetime import date, timedelta
from io import StringIO
from pathlib import Path
from unittest.mock import Mock, call, patch


class MantenimientoTests(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location(
            "frontend_main", Path(__file__).with_name("main.py")
        )
        self.main = importlib.util.module_from_spec(spec)
        # Evitar conexiones a MongoDB incluso durante la carga de la aplicacion.
        with patch("pymongo.MongoClient"):
            spec.loader.exec_module(self.main)
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
                        ajustes.append(call(f"http://localhost:8000/ventas/ajuste/{folio}"))

                with (
                    patch.object(self.main, "db") as db,
                    patch.object(self.main.req, "get") as get,
                    patch.object(self.main.req, "post") as post,
                    patch.object(self.main.pd.DataFrame, "to_csv") as to_csv,
                    redirect_stdout(StringIO()),
                ):
                    get.side_effect = lambda url: Mock(
                        json=Mock(return_value=respuestas[url])
                    )
                    post.return_value.status_code = 200
                    respuesta = self.client.post(
                        "/mantenimiento",
                        data={
                            "fecha_inicio": inicio.isoformat(),
                            "fecha_fin": fin.isoformat(),
                            "sucursal": "desarrollo",
                        },
                    )

                self.assertEqual(respuesta.status_code, 200)
                self.assertEqual(
                    respuesta.get_json(),
                    {
                        "inicio": inicio.isoformat(),
                        "fin": fin.isoformat(),
                        "sucursal": "desarrollo",
                        "total_ventas": sum(dias_con_ventas),
                    },
                )
                self.assertEqual(get.call_args_list, consultas)
                self.assertEqual(post.call_args_list, ajustes)
                self.assertEqual(
                    db.__getitem__.return_value.insert_one.call_args_list, respaldos
                )
                self.assertEqual(to_csv.call_count, sum(dias_con_ventas))


if __name__ == "__main__":
    unittest.main()
