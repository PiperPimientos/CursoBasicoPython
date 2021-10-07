#Con el ciclo For, vamos a ver como hacer recorridos de String
# El caso en el 	que nos ayuda perfectamente este ciclo For, es para recorrer una cadena de strings. Cuando decimos recorrer es porque vamos a tomar una cadena de caracteres por estructuras, y vamos a ir de carácter 1, carácter 2, carácter 4 y sucesivamente.
# 1.	Crearemos un nuevo archivo llamado Recorrer.py
# 2.	Empezamos con nuestras buenas practicas, definiendo una función desde el principio de las líneas de código y despues el entry point
#     a.	Def run():
#                Pass
#      b.	If __name___ = ‘__main__’:
# Run()
# 3.	Vamos a empezar con la lógica de la función run()
#    a.	Creamos una variable nombre con su respectivo input
#    b.	Ahora lo que queremos es tomar ese string que ingresamos como valor de nombre y recorrerlo con un ciclo carácter por carácter. La lógica es, para las letras en el nombre: imprime letra
#         for letra in nombre:
#         print(letra)
#         letra es la variable que va representar a cada uno de los caracteres en  cada una de las repeticiones de nuestro ciclo for.
# 4.	Si imprimimos a este punto, obtendremos lineas de string, por cada letra una línea.



def run():
    # nombre = input('Escribe tu nombre: ')
    # for letra in nombre:
    #     print(letra)
    #Comentamos la funcion que creamos para el primer ejemplo

    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper)


if __name__ == '__main__':
    run()

# Ahora comentaremos todo el contenido de la función y veremos un ejemplo mas en el que volveremos cada letra de una frase en mayuscula, recorriendo cada carácter.

# 1.	Vamos a decirle al usuario que ingrese el valor de una variable que llamaremos frase, esto obviamente lo haremos con un input
# 2.	Luego el ciclo que será for carácter in frase: vamos a imprimir el carácter.upper, es decir que tomaremos cada carácter y lo imprimiremos en mayuscula.
# 3.	Si ejecutamos por ejemplo con: “este es el curso de Python” se imprimen todas las letras en mayuscula, recorriendo letra por letra en cada línea.
