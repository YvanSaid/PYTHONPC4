import requests
import zipfile
import os

def descargar_imagen():
    url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format'
    response = requests.get(url)
    with open('imagen.jpg', 'wb') as file:
        file.write(response.content)
    print("Imagen descargada.")

def crear_zip():
    with zipfile.ZipFile('imagen.zip', 'w') as zipf:
        zipf.write('imagen.jpg')
    print("Imagen zipeada.")

def descomprimir_zip():
    with zipfile.ZipFile('imagen.zip', 'r') as zipf:
        zipf.extractall()
    print("Imagen descomprimida.")

if __name__ == "__main__":
    descargar_imagen()
    crear_zip()
    descomprimir_zip()
