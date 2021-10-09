#Diccionarios, ultima Estructura de tipos de datos del curso

# Es una estructura importante en la carrera como desarrollador. Sin embargo, veremos que despues de terminar las ya vistas estructuras de tipos de datos, encontraremos otras estructuras de tipos de datos como pilas, colas, arboles, etc. Y sin duda, un enorme, gran consejo y sugerencia, es que, ser un experto en tipos de estructuras de datos, nos va  a dar un plus en las entrevistas de trabajo.

# 1.	Construimos nuestra lógica en buenas practicas
# def run():
#       pass
# if __name__ == ‘__main__’:
#        run()
# 2.	Dentro de la lógica de nuestra función run generaremos un diccionario. 
#       La sintaxis de los diccionarios, a diferencia de las listas que son con corchetes y las tuplas que son con paréntesis, es con llaves { }
#       mi_diccionario = { }
#       En JavaScript las llaves sirven para contener objetos, pero en Python las llaves sirven para definir diccionarios.
# 3.	Un diccionario es un tipo de dato de llaves y valores, es decir a diferencia de las listas, no vamos a acceder a los objetos a través de su índice sino a través de sus llaves. Las llaves no necesariamente son numeros que van desde el 0 al infinito
# 4.	Dentro de las llaves podemos definir los valores, la sintaxis, por buenas practicas puede ser dejando de a 4 espacios despues de declarar cada valor nuevo, pero NO es necesario hacer esto en Python, solo por buenas practicas. Asi
#       mi_diccionario = {
#             “llave1”: 1,
#             “llave2”: 2,
#       }
#       Despues de la coma podemos dar enter y trabajar el siguiente elemento, que va estar en la llave2 y llave3
# 5.	Y ahora, si nosotros vemos estos elementos imprimiéndolos en consola, vamos a ver cada uno de los valores delimitados por una llave.
# 6.	Si nosotros queremos llamar un valor, como llamábamos los valores por índice en las listas, lo hacemos con la siguiente sintaxis
#       print(mi_diccionario[])
#       Esto parece como si fueramos a llamar índices, pero la realidad es que dentro de los corchetes, debe ir el nombre de la llave, como por ejemplo ‘llave1’


def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario)
    # Generamos ahora 3 prints para llamar un valor dentro de un diccionario
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    #Hagamos otro ejemplo, por ejemplo, para saber cual es la poblacion de un pais.

    poblacion_paises = {
        'Argentina': 44000000,
        'Colombia': 50000000,
    }
    # print(poblacion_paises['Argentina'])
    #Ahora veremos como hacer para recorrer este diccionario

    # Ahora, si queremos recorrer diccionarios también podemos hacerlo. Vamos a ver como recorrerlo, pero a través de las llaves primero, es decir que queremos que el ciclo for haga 3 vueltas a través del diccionario y nos devuelva el valor de las llaves. Para eso utilizaremos el método .keys(), que nos servirá para acceder al diccionario
    for país in poblacion_paises.keys():
        print(pais)
    
    
    # Pero si queremos imprimir exactamente los valores que tiene el diccionario. En lugar de keys utilizaremos el método .values(), que lo que hace es devolver los valores del diccionario
    for país in poblacion_paises.values():
        print(pais)
    
    # Ya sabemos como recorrer el diccionario y mostrar las llaves tanto como los valores. Pero si queremos hacer un print que nos muestre que cada país tiene tanta población, utilizaremos el método .items() que nos devolverá tanto la llave como el valor y ademas, la sintaxis cambia, pues si queremos acceder a ambos elementos, debemos incluir ambos, separados por comas. Y en el print, concatenar ambos, pero además, cambiando el valor de población, que es un numero entero, por un str, que nos permitirá agregar un mensaje
    for país, poblacion in poblacion_paises.items():
        print(pais + 'tiene' + str(poblacion) + 'habitantes')


if __name__ == '__main__':
    run()


# BONUS:

# Sí quieren hacer más legibles los números grandes como el de las poblaciones pueden hacerlo con _
# población_paises = {
# 	'Argentina': 44_938_712,
# 	'Brasil': 210_147_125,
# 	'Colombia': 50_372_424
# }
