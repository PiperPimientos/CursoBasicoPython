#Vamos a mejorar nuestro Conversor de Monedas
#Aplicaremos funciones para ahorrar todos los bloques de codigo en condicionales que hemos creado
#El objetivo es no repetir todo ese codigo
#En esta funcion concatenaremos el input de la variable pesos con el parametro tipo_pesos adentro


# 1.	Crearemos un ConversorMonedasV3.py para no tocar lo aprendido hasta ese momento
# 2.	Ahora crearemos las funciones, tomemos en cuenta que las funciones deberían ubicarse siempre en el nivel superior del código.
# 3.	Vamos a crear la función def conversor() y en sus parámetros incluiremos primero tipo_pesos porque evidentemente tenemos que saber que tipo de pesos serán esos, luego estará el parámetro valor_dolar
# 4.	Ahora colocaremos nuestra lógica de las condicionales dentro de nuestra función
# 5.	El problema es que tendremos que reemplazar el tipo de pesos para que pueda entenderse como los 3 tipos.
#  A.	Vamos a tener un string solo para “Cuantos pesos”
#  B.	Vamos a tener un string solo para “tienes”
#  C.	Las vamos a concatenar, pero en el medio vamos a colocar otro string que será el parámetro tipo_pesos que asignamos para la función. Y se imprimiría el mensaje automatico, con el tipo de moneda que es
#  D.	Asi mismo vamos a tener que borrar la variable valor_dolar, pues ya vendrá como parámetro
# 6.	Ahora, vamos a invocar nuestra función conversor() dentro de cada uno de los condicionales y vamos a definir los dos parámetros, uno, el tipo_peso entre strings y el otro, valor_dolar será un num que será el valor del dólar en cada uno de los países.


def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_pesos + "colombianos tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas. 
1- Conversor de pesos colombianos a USD
2- Conversor de pesos argentinos a USD
3- Conversor de pesos mexicanos a USD

Ingresa una opcion, 1, 2 o 3: 
"""

opcion = int(input(menu))

if opcion == 1: 
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 98.63)
elif opcion == 3:
    conversor("mexicanos", 20.54)
else:
    print("Ingresa una opcion valida")