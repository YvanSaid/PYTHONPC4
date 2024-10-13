def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith(".py"): #las q estoy haciendo
            print("El archivo no es un archivo Python.")
            return
        with open(ruta_archivo, 'r') as file:
            lineas = file.readlines()
        
        lineas_codigo = [linea for linea in lineas if linea.strip() and not linea.strip().startswith("#")]
        print(f"El archivo {ruta_archivo} tiene {len(lineas_codigo)} líneas de código.")
    
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_archivo}.")

if __name__ == "__main__":
    ruta = input("Ingrese la ruta del archivo Python: ")
    contar_lineas_codigo(ruta)
