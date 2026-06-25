import pandas as pd
import httpx as htx

SERVER = "http://localhost:8000/ventas"

VENTAS_FECHA = f"{SERVER}/?fecha=2026-06-22"

ventas_dia = htx.get(f"{VENTAS_FECHA}")

# Crear un DF con los datos de la respuesta

df = pd.DataFrame(ventas_dia.json())
print("Total de ventas del día:", len(df))
# Guardar en un archivo CSV
df.to_csv("ventas_dia.csv", index=False)
print("El dataframe de ventas del día esta listo")

# El df tiene columnas de folio, numcheque, fecha, facturado, efectivo, tarjeta, etc...
# Convertir la columna 'fecha' a tipo datetime
# Convertir las columnas efectivo y tarjeta en float
# Convertir la columna facturado en boolean

df['fecha'] = pd.to_datetime(df['fecha'])
df['efectivo'] = df['efectivo'].astype(float)
df['tarjeta'] = df['tarjeta'].astype(float)
df['facturado'] = df['facturado'].astype(bool)

# Obtener/filtrar los folios que: facturado = False, efectivo > 120 y tarjeta == 0

folios_filtrados = df[(df['facturado'] == False) & (df['efectivo'] > 120) & (df['tarjeta'] == 0)]['folio']
print("El total de folios filtrados es:", len(folios_filtrados))

folios = pd.DataFrame(folios_filtrados, columns=['folio'])

folios.to_csv("folios_filtrados.csv", index=False)

# Hacer mant
MANTENIMIENTO = f"{SERVER}/ajuste"

for folio in folios_filtrados:
    ajuste = htx.post(f"{MANTENIMIENTO}/{folio}")
    print(ajuste.text)

print("Las ventas fueron ajustadas con el nuevo algoritmo")