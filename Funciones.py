#Funciones en python

# 1.	Haremos un print(“Mensaje especial: “)
# 2.	Haremeos otro print(“Estoy aprendiendo a usar funciones”)
# 3.	Repetiremos este par de lineas dos veces mas.
# 4.	Si ejecutamos el programa nos daremos cuenta que estamos repitiendo la logica tres veces. ¿Cómo podemos escribir la logica una sola vez para despues ejecutarla 3 veces?
# 5.	Vamos a escribir la siguiente sintaxis, palabra reservada + nombre/identificador de la funcion + par de parentesis + dos puntos
#  def imprimir_mensaje():
#     Luego sigue el identado, 
# 6.	Dentro de la funcion pondremos la logica que construimos 
# 7.	Eliminamos todo el bloque de codigo anterior
# 8.	Ahora, si queremos ejecutar ese codigo tres veces, en vez de ejecutar esos print, lo que podemos hacer es escribir el identificador imprimir_mensaje() y ya con eso estamos invocando la funcion, que en realidad quiere decir que nos vamos a la definicion de la funcion (por eso viene la palabra def) y ejecutamos la logica que esta adentro.
# 9.	Si lo que hacemos es invocar esa funcion tres veces y luego ejecutamos esa funcion en la consola, veremos que el mensaje aparece tres veces

# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

#Dejaremos este bloque de codigo como referencia, comentado





#Parametros de las Funciones en Python


# 1.	Crearemos una variable opción que va tener asignado un int(input(“Elige una opción (1, 2, 3): “))
# 2.	Con if preguntaremos, si la opción es igual a 1, voy a ejecutar print(“Hola”), print(“Como estas”), print(“Elegiste la opción 1”), print(“Adios”)
# 3.	Elif si la opción es igual a 2, voy a poner los mismos print
# 4.	Elif con la opción 3, igual
# 5.	Else print(“Escribe la opción correcta”)
# 6.	Si ejecutamos, ya sabemos lo que pasa
# 7.	Estoy repitiendo la misma logica de siempre. Lo único que cambia es el print que nos dice “Escogiste la opción X”
# 8.	Como cambiamos esto con funciones?
# a.	Crearemos una función llamada conversación def conversación()
#    b.	Dentro de los paréntesis vamos a colocar los parámetros, que no son mas que variables que tendremos disponibes para usar dentro de la función.
#    c.	A ese parámetro le daremos el nombre de mensaje
#    d.	Una vez tenga eso, vamos a cortar y pegar dentro de la funcion toda la lógica del bloque de código que habíamos construido
# 9.	Ahora borraremos todos los bloques de código de nuestras condicionales y en vez de esa lógica, colocaremos la función directamente, que es conversación().
#    a.	Como dentro de los paréntesis teníamos un parámetro, ahora solo es definirlo¸ será (“elegiste la opción 1’) y asi con cada uno de los 3 mensajes 
# 10.	 Si ejecutamos veremos como ahora simplemente pasa por los condicionales y listo. 



def conversacion(mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("Escribe la opcion correcta")