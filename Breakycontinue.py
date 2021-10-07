#Veremos como hacer para ejecutar determinadas vueltas de un ciclo o
#frenarlo en cierta repeticion del ciclo/bucle, con las palabras Break y Continue

# En un primer ejemplo
# Vamos a hacer tres ciclos de tipo For, para ver como funcionan estas palabras claves

# 1.	Vamos a trabajar esta lógica: para el contador en el rango que va del 0 al 999, vamos a imprimir el contador, pero la diferencia es que aquí, en vez de imprimir todos los números del 0 al 999, vamos es a imprimir solo los números pares, los impares NO.
# Para esto incluiremos antes de ese print de contador
#        a.	Si el contador modulo 2 es distinto de 0, voy a continuar
#        If contador % 2 != 0:
#                continue
#         Con esto quisimos decir que si el contador al dividirlo por 2, el resto de la división no es 0, voy a saltarme esta vuelta del ciclo y lo que esta despues de la palabra continue, no se va ejecutar. Esto es porque todo numero que dividido por dos, tenga un resto distinto que 0, es un numero impar.
# 2.	En resumen, tendremos un ciclo que ejecute del 0 al 999, pero que cada vez que se encuentre con la condición de contador, es decir que sea numero impar, nos vamos a saltar la vuelta del ciclo y no vamos a imprimir ese contador.
#En resumen continue es bastante sencillo, lo que quiere decir que despues de continue, lo que viene despues no se va ejecutar y pasamos a la siguiente vuelta del ciclo.


	

# Aprendamos ahora que hacemos con la palabra clave break. 

# 1.	Vamos a comentar el código de ejemplo de continue
# 2.	La lógica será para la variable i, del rango que va del 0 al 9999: 
#       Si la variable i es igual al numero 5678, 
#       entonces break
#       Nota: el identificador i para los ciclos for, es un estándar entre desarrolladores. Muchas veces cuando nosotros queremos hacer ciclos, la variable que va ir cambiando de valor, va tener el nombre i y esto lo veremos en casi todos los lenguajes de programación. 
# 3.	Ademas, antes de esa condicional para i, vamos a imprimir la variable i. Para que comience a imprimirse antes de que se ejecute la condicional

# Ahora veremos un ejemplo mas de break pero con los recorridos de strings

# 1.	Comentamos todo el ejemplo anterior
# 2.	Creamos una variable texto que obtendrá su valor del input de Escribe un texto:
# 3.	Ahora crearemos un ciclo que tendrá la lógica de para letra en texto:
#       Si letra es igual a ‘o’, entonces break
#       Luego imprime, despues de esa condicional letra
# 4.	Esto es, que introducimos un texto, el ciclo va recorrer ese string y cuando el ciclo se encuentre con la letra o entonces se va romper break y vamos a imprimir a esa letra.
# 5.	Si introducimos un texto como ‘Estoy grabando el curso de Python”, imprimiría solamente
#       e
#       s
#       t
#       Y cuando se cuentra con la o, se frena el ciclo


def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    # print(contador)
    #Comentamos todo el ejemplo continue y ahora veremos el ejemplo para break

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    #Comentamos todo este primer ejemplo break, en el que se rompe el ciclo en el numero 5678
    #Ahora veremos un ejemplo de break pero recorriendo un string

    # texto = input('Introduce un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)
    #Ahora comentaremos este ejemplo de break
    #Lo siguiente es el reto de utilizar while con break y continue

    mult_number = int(input('Ingresa un numero para multiplicar en bucle hasta 15: '))
    
    for contador in range(1000):
            while contador < 16:
                print(mult_number * contador)
                break

if __name__ == '__main__':
    run()



