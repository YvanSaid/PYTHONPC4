import csv
import sqlite3

def leer_ventas(archivo_csv):
    ventas = []
    with open(archivo_csv, newline='', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            fecha, producto, cantidad, precio_usd = row[0], row[1], int(row[2]), float(row[3])
            ventas.append({'fecha': fecha, 'producto': producto, 'cantidad': cantidad, 'precio_usd': precio_usd})
    return ventas

def obtener_tipo_cambio(fecha, conexion):  #SQLite
    cursor = conexion.cursor()
    cursor.execute("SELECT tasa FROM tipo_cambio WHERE fecha = ?", (fecha,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else None  # Devuelve la tasa o None si no existe

def calcular_totales(ventas, conexion):
    totales = {}
    for venta in ventas:
        tipo_cambio = obtener_tipo_cambio(venta['fecha'], conexion)
        
        if tipo_cambio is None:
            print(f"No se encontró tipo de cambio para la fecha {venta['fecha']}.")
            continue

        precio_total_usd = venta['cantidad'] * venta['precio_usd']
        precio_total_soles = precio_total_usd * tipo_cambio

        if venta['producto'] not in totales:
            totales[venta['producto']] = {'usd': 0, 'soles': 0}
        
        totales[venta['producto']]['usd'] += precio_total_usd
        totales[venta['producto']]['soles'] += precio_total_soles

    return totales

def mostrar_totales(totales):
    for producto, precios in totales.items():
        print(f"Producto: {producto}")
        print(f"  Precio total en USD: ${precios['usd']:.2f}")
        print(f"  Precio total en Soles: S/.{precios['soles']:.2f}")
        print("-" * 30)


def main():
    conexion = sqlite3.connect('base.db')
    
    ventas = leer_ventas('ventas.csv')
    
    totales = calcular_totales(ventas, conexion)   

    mostrar_totales(totales)
    
    conexion.close()

if __name__ == "__main__":
    main()
