import requests
import sqlite3

def obtener_tipo_cambio():
    url = 'https://apis.net.pe/api-tipo-cambio.html'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Conexión a SQLite
        conexion = sqlite3.connect('base.db')
        cursor = conexion.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS sunat_info (fecha TEXT, compra REAL, venta REAL)')
        
        for registro in data:
            cursor.execute('INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)',
                           (registro['fecha'], registro['compra'], registro['venta']))
        
        conexion.commit()
        cursor.close()
        print("Datos almacenados en la base de datos.")
    
    except requests.RequestException as e:
        print(f"Error al consultar la API: {e}")

if __name__ == "__main__":
    obtener_tipo_cambio()
