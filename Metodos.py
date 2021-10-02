#Metodos

#Supongamos que alguien ingresa un nombre, y lo ingresa en minúscula, sabemos que en realidad el nombre tiene que estar con la letra inicial en mayuscula. Estos datos se recogen por ejemplo cuando tu eres un backend developer.
# Hay que aprender a hacer este tipo de cosas desde ahora, para eso tenemos un concepto nuevo que son los Métodos.
# 1.	Vamos a crear una variable identificada como nombre, que tenga asignado un input que nos pregunte cual es nuestro nombre.
# 2.	Cuando Python nos pregunte, le respondemos todo en minúsculas Felipe
# 3.	Para solucionar esto utilizamos nombre.upper() esto es un método, es una función que es especial para un tipo de dato en particular y tiene una función asociada, que es colocar este texto en mayúsculas.
# 4.	Si ejecutamos, ahora nos aparecerá FELIPE, todo en mayúsculas.
# 5.	Sin embargo no es lo que  yo buscaba, que es colocar la primera letra en mayúsculas y las siguientes en minúsculas. Esto lo logramos con el método .capitalize. y ahí si nos devolverá Felipe 
# 6.	Lo que tenemos que tener en cuenta es que los métodos nos devuelven valores, pero no guardan dicho valor en memoria. Si nos fijamos que hay dentro de nombre, veremos que seguimos teniendo como valor Felipe
#       Para evitar esto, lo que hay que hacer es reasignar a nombre, el método nombre = nombre.capitalize() si hacemos esto ahora si quedara asignado a la variable nombre, el valor ‘Felipe ‘
# 7.	Veamos que intencionalmente dejamos un espacio en nuestra variable nombre ‘Felipe ‘, para solucionar esto utilizaremos otro método llamado strip() que lo que hace es eliminar los espacios basura que pueden estar al principio o al final del string.
# 8.	Otro método interesante es lower() que nos servirá para transformar el string en minúsculas todas
# 9.	Otro método interesante es el replace() que nos servirá para reemplazar un valor determinado dentro de ese valor guardado, por ejemplo si queremos reemplazar todas las letras e de Felipe por letras i esta es la sintaxis nombre.replace(‘e’, ‘i’) y me quedara Filipi
# 10.	 Y si yo quisiera acceder a cada letra en particular de mi variable nombre, utilizaremos índices, para esto tendremos que utilizar los corchetes [ ] entonces si escribimos el identificador nombre[ ] y entre corchetes ponemos un 0, Python nos regresa la letra F, que seria la letra 0. E incluso puedo guardar variables como primera_letra = nombre[0] 
# 11.	 Tambien podemos averiguar cuantos caracteres tiene mi string con el metodo len() y si lo hacemos por ejemplo con la variable que acabamos de crear len(primera_letra) nos va imprimir un 1, que es la cantidad de caracteres que tiene el string o incluso podríamos hacerlo colocando la string directamente sin variable len(“Hola Mundo”) nos debe imprimir un 9
# En resumen, los métodos son funciones que no hemos tenido que construir porque son built-in, vienen ya construidas dentro de python


nombre = input("Cual es tu nombre?: ")
#Ejecutamos: ingresamos 'felipe ', con el espacio

nombre.upper()
nombre.capitalize()
#Si ejecutamos directamente nos devuelve los valores, pero no guarda en memoria, para que guarde:
nombre = nombre.capitalize()
nombre = nombre.strip()
nombre = nombre.lower()
nombre = nombre.replace('e', 'i')

#Los indices
nombre[0] #Nos devuelve la letra F
primera_letra = nombre[0] #Guarda una variable con el valor 'F'

#averiguar cuantos caracteres tiene el string
len(primera_letra) #Nos devuelve un 1 que es la cantidad de caracteres en esa variable

