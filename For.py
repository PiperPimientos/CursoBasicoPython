#Veremos ahora el ciclo For, despues de haber trabajado While en Bucles.py

# El profesor nos plantea un problema: imprimir los números del 1 al 1000.

# Si lo hiciéramos de manera normal tendríamos que hacer desde print(1) hasta print(1000)

# Pero si lo queremos hacer con bucles, pues lo hacemos de esta forma

# 1.	Creamos una variable contador. Nota: cada rato nos vamos a encontrar con una variable contador en la lectura de código, que significa que va ir aumentandose progresivamente.
#       Le vamos a poner como valor inicial, en este caso, el 1.
# 2.	Vamos a hacer un print de contador
# 3.	Ahora viene el while contador < 1000 vamos a sumarle un valor al contador
#       a.	Contador = contador + 1. Hay un pequeño truco en esta línea, cuando nosotros vamos a aumentar una variable un numero determinado de veces, en vez de escribir todo esto, podríamos escribir contador += 1
#       b.	Print(contador)
# 4.	Va pasar esto en bucle hasta que lleguemos a esa condición de que contador sea menor a 1000.

# contador = 1
# print(contador)
# while contador < 1000:
#     contador += 1
#     print(contador)


# Hasta aquí ya vimos como resolver el problema de manera tradicional, ahora lo resolveremos con el ciclo For

# 1.	La sintaxis es for contador in range(1000):
#    a.	print(contador) 
# 2.	Esta sencilla línea de código se traduce en: para la variable contador, en el rango de 1000, imprime contador.

# Para entender lo de los range o rangos, hay que saber que si yo asigno una variable a = range(1000) al imprimir nos dira que la variable a tiene el valor entre 0 y 1000.

# Si lo convertimos en una lista a = list(range(1000)), al imprimir nos mostrara en una lista los números desde el 0 al 999. A propósito de esto, entonces tendríamos que redefinir que queremos que el rango sea hasta 1001, porque o sino, el ciclo va parar justo en 999, con el valor inicial no hay problema, siempre partira desde ahí. E incluso, podríamos asignar cualquier valor inicial de partida en el ciclo con esta sintaxis for contador in range(1, 1001) y ya no partiría desde 0 sino desde 1.

for contador in range(1, 1001):
    print(contador)

#Incluso podriamos hacer la tabla de un numero, por ejemplo el 11 hasta el 9

for i in range(10):
    print(11 * i)

#Nota: Es indistinto utilizar la palabra ciclo o bucle, significan lo mismo