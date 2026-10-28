import random

def get_sustituno() -> tuple[dict, int]:

    # Definir productos
    productos: dict[str, dict] = {
        "cacahuate espanol": {
            "id": "3126004",
            "precio": 25,
            "preciosinimpuestos": 21.55,
            "categoria": "alimentos",
            "impuesto": 16.00
        },
        "hot nuts": {
            "id": "3131003",
            "precio": 25,
            "preciosinimpuestos": 21.55,
            "categoria": "alimentos",
            "impuesto": 16.00
        },
        "brownie": {
            "id": "3119003",
            "precio": 39 ,
            "preciosinimpuestos": 33.62,
            "categoria": "alimentos",
            "impuesto": 16.00
        },
        "panque" :{
            "id": "3119005",
            "precio": 40,
            "preciosinimpuestos": 34.48,
            "categoria": "alimentos",
            "impuesto": 16.00
        },
        "americano" :{
            "id": "3121003",
            "precio": 39,
            "preciosinimpuestos": 33.62,
            "categoria": "bebidas",
            "impuesto": 16.00
        },
        "latte" :{
            "id": "3127003",
            "precio": 55,
            "preciosinimpuestos": 47.,
            "categoria": "bebidas",
            "impuesto": 16.00
        },
        
    }
    
    pesos = [25, 15, 10, 20, 15, 15]  # Pesos correspondientes a cada producto
    """
    Cafe 1/4 -> 25%
    Cafe 1/2 -> 15%
    Pan -> 10%
    Pepino limon y chia -> 20%
    Jamaica frutos rojos -> 15%
    Naranjada fresa y albahaca -> 15%
    """
    prod_key = random.choices(list(productos.keys()), weights=pesos)[0] # Se elige un producto aleatorio basado en los pesos definidos
    cantidad = random.randint(1, 3) # Se genera una cantidad aleatoria entre 1 y 3
    return productos[prod_key], cantidad

if __name__ == "__main__":
    for _ in range(10):
        producto_info, cantidad = get_sustituno()
        print(f"Producto: {producto_info}, Cantidad: {cantidad}")