#Bucles en python.

# Si quisiéramos hacer por ejemplo varias potencias de un numero hasta llegar a un resultado deseado, pero de la manera tradicional, sin usar los bucles:
#    1.	Vamos a hacer todas las potencias de 2 hasta llegar a 1000. Y luego todas las potencias de 2 hasta llegar al 1000000.
#    2.	Podríamos para esto crear una variable llamada contador a la cual le pondremos como valor 0
#    3.	Luego print(‘2 elevado a ‘ + str(contador) + ‘ es igual a: ‘ + str(2**contador))
#    4.	Como la primera potencia seria 2 elevado a 0, daría como resultado 1. Luego si empezamos a repetir pero guardando como valor de contador un numero mayor, empezaremos a hacer la potencia mas grande, 2 elevado a la 1(valor de contador) te daría 2, luego 2 elevado a la 2(valor de contador) te daría 4, y asi sucesivamente hasta llegar a mil o 1 millon como queremos 

# contador = 0
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))

# contador = 1
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))

# contador = 2
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))

# contador = 3
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))

# contador = 4
# print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2** contador))

#Asi hasta llegar a 1000
#Para resolver este problema de repetir tanto codigo, usaremos bucles



# Dentro de la programacion tenemos varios tipos de bucles. El primero es while, que significa mientras. 

# 1.	Comentamos todas las líneas del ejemplo que hicimos.
# 2.	Ahora definimos una función principal que tendrá como nombre run.
# 3.	Ahora nuestro entry point que será if __name__ ==  ‘__main__’:
# 4.	Dentro de nuestra función vamos a resolver el problema
#    a.	Lo primero sera crear la variable que nos defina ese numero al que queremos llegar en la potencia, que será 1000, para ello limite = 1000, algo que debemos aprender es que si queremos hacer una constante y no una variable, el identificador debe ir en mayúsculas como LIMITE = 1000, lo que tenemos que saber, es que ya no se podra reasignar en otro valor
#    b.	Ahora vamos a asignar a nuestra variable contador un valor de 0 y esta será la variable que ira aumentando el numero de potencias de 2, tantas veces como contador lo diga
#    c.	Luego definimos la variable potencia_2 = 2**contador que será la variable que nos guardara la potencia que se realizara
#    d.	Ahora viene el ciclo que seria con while y luego llamar a potencia_2 para decir que si es menor que < la constante LIMITE entonces suceda lo siguiente. Si lo detallamos bien, de hecho, la sintaxis es la misma que con las condicionales.
#       Decimos entonces, que while potencia_2 < LIMITE vamos a ejecutar:
#       print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
#       Si la condición de while siempre es True, se nos va presentar el problema del infinite loop o bucle infinito. Para resolver esto, dentro del bucle, diremos que contador = contador + 1 y de esta manera, no se quedara contador de manera inifinita ejecutando el 0 que tiene como valor.
#       Finalmente tenemos que definir otra vez potencia_2 = 2**contador, de esta manera, potencia de 2 va utilizar el valor nuevo que tenga contador cuando se le sume un 1.

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()