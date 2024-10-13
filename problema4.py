import requests

def procesar_temperaturas():
    url = 'https://raw.githubusercontent.com/gdelgador/ProgramacionPython202407/main/Modulo4/src/temperaturas.txt'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  #Verificar
        
        lineas = response.text.strip().split('\n')
        
        temperaturas = [float(linea.split(',')[1].strip()) for linea in lineas]
        promedio = sum(temperaturas) / len(temperaturas)
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)
    
        with open('resumen_temperaturas.txt', 'w') as resumen:
            resumen.write(f"Temperatura promedio: {promedio:.2f}°C\n")
            resumen.write(f"Temperatura máxima: {max_temp:.2f}°C\n")
            resumen.write(f"Temperatura mínima: {min_temp:.2f}°C\n")
        
        print("Resultados guardados en resumen_temperaturas.txt")
    
    except requests.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

if __name__ == "__main__":
    procesar_temperaturas()
