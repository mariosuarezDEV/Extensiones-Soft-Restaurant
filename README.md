# API de Ventas - Cheques

Esta API expone endpoints para consultar **ventas** (cheques) y sus detalles.  
Está desarrollada con **Django REST Framework** e implementa **caché en Redis/Memcached** para optimizar las consultas (con expiración de 24 horas).

## Endpoints

### 1. Listar Ventas por Fecha

Obtiene todas las ventas registradas en una fecha específica.

**URL**
```
GET /ventas/
````

**Parámetros Query**
| Nombre | Tipo   | Requerido | Descripción |
|--------|--------|-----------|-------------|
| fecha  | string (YYYY-MM-DD) | ✅ | Fecha de las ventas a consultar |

**Ejemplo de petición (httpie)**
```bash
http GET http://127.0.0.1:8000/ventas/?fecha==2025-08-27
````

**Respuesta exitosa (200)**

```json
[
  {
    "folio": 64229,
    "fecha": "2025-08-27T13:45:00Z",
    "cliente": "Juan Pérez",
    "total": "250.50"
  },
  {
    "folio": 64230,
    "fecha": "2025-08-27T14:10:00Z",
    "cliente": "María López",
    "total": "320.00"
  }
]
```

**Errores**

* `400 Bad Request` → Si no se envía el parámetro `fecha`.

---

### 2. Detalle de una Venta

Obtiene la información completa de una venta, incluyendo consumo (detalles) y pagos.

**URL**

```
GET /ventas/{folio}/
```

**Parámetros de Ruta**

| Nombre | Tipo | Requerido | Descripción                     |
| ------ | ---- | --------- | ------------------------------- |
| folio  | int  | ✅         | Identificador único de la venta |

**Ejemplo de petición (httpie)**

```bash
http GET http://127.0.0.1:8000/ventas/64229/
```

**Respuesta exitosa (200)**

```json
{
  "Venta": {
    "folio": 64229,
    "fecha": "2025-08-27T13:45:00Z",
    "cliente": "Juan Pérez",
    "total": "250.50"
  },
  "Consumo": [
    {
      "producto": "Café Americano",
      "cantidad": 2,
      "precio": "30.00",
      "subtotal": "60.00"
    },
    {
      "producto": "Sandwich",
      "cantidad": 1,
      "precio": "50.00",
      "subtotal": "50.00"
    }
  ],
  "Pago": [
    {
      "metodo": "Efectivo",
      "monto": "110.50"
    },
    {
      "metodo": "Tarjeta",
      "monto": "140.00"
    }
  ]
}
```

**Errores**

* `404 Not Found` → Si el `folio` no existe.

---

## Cache

* Cada petición se guarda en caché durante **24 horas (86400 segundos)**.
* Claves de caché usadas:

  * `ventas_{fecha}`
  * `detalle_venta_{folio}`

---

## Ejecución local

1. Levantar el servidor de Django:

   ```bash
   python manage.py runserver
   ```

2. Probar los endpoints con httpie o cURL.
