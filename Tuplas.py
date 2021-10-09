#Las Tuplas
# Las tuplas son otro tipo de estructuras de datos. 

# 1.	Primero veremos un truco que nos falto repasar de las Listas. Esto es la concatenación de listas.
#       Si creamos por ejemplo numeros2 = [6, 7, 8, 9]
#       Y mantenemos la lista que teníamos del ejemplo en listas, es decir, numeros = [1, 2, 3, 4, 5]
#       Podemos concatenar ambas listas y guardarlas en una lista final 
#       lista_final = numeros + numeros2
# nos mostraria ambas listas en una sola.
# 2.	Tambien podemos multiplicar las listas y su valor aparecerá repetido cuantas veces lo hayamos multiplicado
#       numeros * 5


# Ahora bien, las tuplas, son una manera ineficiente de trabajar con listas en Python, porque las listas son dinámicas; las listas son un tipo de dato muy dinamico, en cambio, las tuplas no y no consumen tantos recursos como las listas.

# 1.	La sintaxis de las tuplas es casi la misma de las listas, pero en vez de corchetes, son paréntesis
#       mi_tupla = (1, 2, 3, 4)
# 2.	La diferencia es que si queremos hacer por ejemplo métodos con las tuplas, no vamos a poder hacerlo. Esto es porque las tuplas son un tipo de objeto especial que nosotros vamos a llamar estáticos
# 3.	Cuando nosotros hacemos iteraciones, es decir, recorremos listas con el ciclo for, se va iterar mucho mas rápido que las listas.
#       for elemento in mi_tupla:
#           print(elemento)

# NOTA: ademas de las tuplas, tenemos otros objetos inmutables en Python, estos son, por ejemplo, los string, que al tratar de agregarle otro carácter, no vamos a poder.

