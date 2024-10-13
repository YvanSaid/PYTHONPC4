import requests

def obtener_precio_bitcoin(n):
    try:
        #Consulta la API de CoinDesk segun el ejercicio
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  #Se obtiene una excepción para códigos de estado HTTP inválidos
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        total = n * precio_usd
        print(f'El costo de {n} bitcoins es: ${total:,.4f}')
    except requests.RequestException as e:
        print(f"Error al consultar la API: {e}")

if __name__ == "__main__":
    n = float(input("Ingrese la cantidad de Bitcoins: "))
    obtener_precio_bitcoin(n)
