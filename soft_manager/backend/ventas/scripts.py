import random

def get_sustituno() -> tuple[dict, int]:

    # Definir productos
    productos: dict[str, dict] = {
        "cafe 1/4": {
            "id": "V-034003",
            "precio": 100
        },
        "cafe 1/2": {
            "id": "V-034002",
            "precio": 195
        },
        "pan": {
            "id": "042035",
            "precio": 65
        }
    }
    
    pesos = [40, 40, 20]  # Pesos correspondientes a cada producto
    prod_key = random.choices(list(productos.keys()), weights=pesos)[0] # Se selecciona un producto al azar de manera segura
    cantidad = random.randint(1, 3) # Se genera una cantidad aleatoria entre 1 y 3
    return productos[prod_key], cantidad

producto_info, cantidad = get_sustituno()

print(f"Producto seleccionado: {producto_info['id']}, Precio: {producto_info['precio']}, Cantidad: {cantidad}")