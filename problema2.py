import random
from pyfiglet import Figlet # type: ignore

def imprimir_figlet():
    figlet = Figlet()
    
    fuentes = figlet.getFonts()
    print("Estas son algunas fuentes admitidas por FIGlet:")
    
    #Mostrar una lista de fuentes disponibles
    for i, fuente in enumerate(fuentes[:10], 1): 
        print(f"{i}. {fuente}")
    
    fuente = input("Ingrese el nombre de una fuente (o presione Enter para seleccionar una fuente aleatoria): ")
    
    if not fuente:
        fuente = random.choice(fuentes)
        print(f"Se seleccionó la fuente aleatoria: {fuente}")
    
    try:
        figlet.setFont(font=fuente)
    except Exception as e:
        print(f"Error al configurar la fuente: {e}")
        return
    
    texto = input("Ingrese el texto que desea imprimir: ")
    
    print(figlet.renderText(texto))

if __name__ == "__main__":
    imprimir_figlet()
