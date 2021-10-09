#Vamos a ver las LISTAS en python

# #Como guardar distintos tipos de datos en una sola variable? Es a través de las listas, las listas pertenecen a un conjunto llamado estructuras de datos que son formas que nos brindan los lenguajes de programación para guardar varios valores en una variable, pero con diferente formato.


# 1.	Creamos un archivo llamado Listas.py
# 2.	Las listas se expresan con la siguiente sintaxis, si por ejemplo queremos una variable llamada números que contenga varios números
#        numeros = [ ] igual que como hacíamos los índices de strings, y adentro colocaremos los numeros ordenadamente, separados por comas
# 3.	Si imprimimos, nos mostrara esa misma lista entre los corchetes.
# 4.	A la vez, podríamos crear listas que contengan distintos tipos de datos, como strings, boleanos, enteros, flotantes, etc..
#       objetos = [‘Hola’, 1, True, False, 2.3]
# 5.	Para acceder a cada dato, tengo que llamar entre corchetes el numero en el que esta asignado, por ejemplo si en el ejemplo anterior queremos llamar Hola
#        objetos = [0]
# 6.	Si yo quiero agregar otro objeto a esa lista, puedo hacerlo con un método, recordemos que los métodos nos permiten traer funciones que ya están construidas y, que las listas tienen distintos tipos de métodos
#       Para este caso utilizaremos .append() y si por ejemplo queremos agregar otro booleano False, lo hacemos asi
#       objetos.append(False)
# 7.	Si quiero borrar algo, lo hago con el método .pop() y entre paréntesis especificando el índice del elemento que queremos borrar. Por ejemplo si queremos borrar Hola
#       objetos.pop(0)
# 8.	Si por ejemplo quiero recorrer toda la lista, lo haremos con el ciclo For, imprimiéndonos un elemento en cada línea de impresión.
#       for elemento in objetos:
#             print(elemento)
# 9.	E incluso podría utilizar los slices en las listas, para poder por ejemplo invertir el orden de la lista.
#       objetos[::-1]
#       o ir desde el índice X al índice Y por ejemplo
#       objetos[1:3]

