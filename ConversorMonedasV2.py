#Conversor de Monedas V2. Incluimos peso argentino y mexicano

#El codigo original se puede ver en el archivo ConversorMonedas.py
#Pasos: 1-Creamos un menu donde introducimos el programa y opciones
# 2-Creamos un input para elegir una de las tres opciones del menu
# 3-Introducimos las condicionales para la eleccion de una de las tres opciones
# 4-Adaptamos el codigo que ya teniamos para cada condicion

menu = """
Bienvenido al conversor de monedas. 
1- Conversor de pesos colombianos a USD
2- Conversor de pesos argentinos a USD
3- Conversor de pesos mexicanos a USD

Ingresa una opcion, 1, 2 o 3: 
"""

opcion = int(input(menu))

if opcion == 1: 
    pesos = input("Cuantos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos argentinos tienes? ")
    pesos = float(pesos)
    valor_dolar = 98.63
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 20.54
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Ingresa una opcion valida")