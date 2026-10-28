from django.test import SimpleTestCase

from . import prodsuc, scripts
from .views import fuente_productos


class FuenteProductosTests(SimpleTestCase):
    def test_anahuac_usa_scripts(self):
        self.assertIs(fuente_productos("anahuac"), scripts)

    def test_anahuac_sin_importar_mayusculas_ni_espacios(self):
        self.assertIs(fuente_productos(" Anahuac "), scripts)

    def test_otras_sucursales_usan_prodsuc(self):
        for sucursal in ("centro", "araucarias", "desarrollo", "", None):
            with self.subTest(sucursal=sucursal):
                self.assertIs(fuente_productos(sucursal), prodsuc)

    def test_ambas_fuentes_devuelven_producto_y_cantidad(self):
        for fuente in (scripts, prodsuc):
            with self.subTest(fuente=fuente.__name__):
                producto, cantidad = fuente.get_sustituno()
                self.assertIn("id", producto)
                self.assertIn("precio", producto)
                self.assertIn("preciosinimpuestos", producto)
                self.assertIn("categoria", producto)
                self.assertIn("impuesto", producto)
                self.assertTrue(1 <= cantidad <= 3)
