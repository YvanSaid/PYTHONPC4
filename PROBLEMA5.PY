def guardar_tabla_multiplicar(n):
    """Genera un archivo con la tabla de multiplicar del número n"""
    with open(f'tabla-{n}.txt', 'w') as file:  # guarde en un fichero con el nombr tabla-n.txt
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en 'tabla-{n}.txt'.")


def mostrar_tabla(n):
    """Lee y muestra el contenido de la tabla de multiplicar desde el archivo tabla-n.txt"""
    try:
        with open(f'tabla-{n}.txt', 'r') as file:
            print(f"Tabla de multiplicar del {n}:")
            print(file.read())
    except FileNotFoundError:
        print(f"No se encontró el archivo 'tabla-{n}.txt'. Por favor, genera la tabla primero.")


def mostrar_linea_tabla(n, m):
    """Muestra la línea m de la tabla de multiplicar n si el archivo existe"""
    try:
        with open(f'tabla-{n}.txt', 'r') as file:
            lineas = file.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m} de la tabla del {n}: {lineas[m-1].strip()}")
            else:
                print("El número de línea debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"No se encontró el archivo 'tabla-{n}.txt'. Por favor, genera la tabla primero.")


def main():
    while True:
        print("\nMenú:")
        print("1. Generar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar una línea específica de la tabla")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            # Generar tabla de multiplicar
            try:
                n = int(input("Ingrese un número entre 1 y 10 para generar su tabla de multiplicar: "))
                if 1 <= n <= 10:
                    guardar_tabla_multiplicar(n)
                else:
                    print("Por favor, ingrese un número entre 1 y 10.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        elif opcion == "2":
            # Mostrar tabla de multiplicar
            try:
                n = int(input("Ingrese un número entre 1 y 10 para mostrar su tabla de multiplicar: "))
                if 1 <= n <= 10:
                    mostrar_tabla(n)
                else:
                    print("Por favor, ingrese un número entre 1 y 10.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        elif opcion == "3":
            # Mostrar una línea específica de la tabla
            try:
                n = int(input("Ingrese un número entre 1 y 10 para la tabla de multiplicar: "))
                m = int(input(f"Ingrese el número de línea que desea mostrar (1-10) de la tabla del {n}: "))
                if 1 <= n <= 10 and 1 <= m <= 10:
                    mostrar_linea_tabla(n, m)
                else:
                    print("Por favor, ingrese números entre 1 y 10.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        elif opcion == "4":
            # Salir
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")


if __name__ == "__main__":
    main()
