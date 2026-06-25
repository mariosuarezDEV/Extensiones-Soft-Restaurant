import random

def get_sustituno() -> tuple[dict, int]:

    # Definir productos
    productos: dict[str, dict] = {
        "cafe 1/4": {
            "id": "V-034003",
            "precio": 100,
            "preciosinimpuestos": 100,
            "categoria": "otros",
            "impuesto": 0
        },
        "cafe 1/2": {
            "id": "V-034002",
            "precio": 195,
            "preciosinimpuestos": 195,
            "categoria": "otros",
            "impuesto": 0
        },
        "pan": {
            "id": "042035",
            "precio": 65,
            "preciosinimpuestos": 65,
            "categoria": "otros",
            "impuesto": 0
        },
        "pepino limon y chia" :{
            "id": "031013",
            "precio": 54,
            "preciosinimpuestos": 46.55,
            "categoria": "bebidas",
            "impuesto": 16.00
        },
        "jamaica frutos rojos" :{
            "id": "031015",
            "precio": 54,
            "preciosinimpuestos": 46.55,
            "categoria": "bebidas",
            "impuesto": 16.00
        },
        "naranjada fresa y albahaca" :{
            "id": "031017",
            "precio": 54,
            "preciosinimpuestos": 46.55,
            "categoria": "bebidas",
            "impuesto": 16.00
        },
        
    }
    
    pesos = [25, 25, 10, 15, 10, 15]  # Pesos correspondientes a cada producto
    """
    Cafe 1/4 -> 25%
    Cafe 1/2 -> 25%
    Pan -> 10%
    Pepino limon y chia -> 15%
    Jamaica frutos rojos -> 10%
    Naranjada fresa y albahaca -> 15%
    """
    prod_key = random.choices(list(productos.keys()), weights=pesos)[0] # Se elige un producto aleatorio basado en los pesos definidos
    cantidad = random.randint(1, 3) # Se genera una cantidad aleatoria entre 1 y 3
    return productos[prod_key], cantidad

if __name__ == "__main__":
    for _ in range(10):
        producto_info, cantidad = get_sustituno()
        print(f"Producto: {producto_info}, Cantidad: {cantidad}")