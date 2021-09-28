#Veremos cuales son los operadores aritmeticos
#Suma
5 + 5
#En consola, press enter y de una sale el resultado
#Desde el editor de codigo hay que hacer un print
print(5 + 5)
#Podemos restar
5 - 5
#en la consola sale directo 0
#multiplicar
5 * 2
#dividir
10 / 2
#Division entera
10 // 2
#sacar el modulo, que es el numero que nos permite ver el resto de la division
10 % 2
#elevar al exponente
2 ** 2





#Tenemos que saber que Python tiene la regla de precedencia de operadores: si ponemos operación como  5 + 5 * 2, lo que se tendría que resolver primero es la multiplicación. Se resuelven primero los paréntesis, luego las potencias y raíces, multiplicaciones y divisiones y ultimo sumas y restas.
#PEMDAS: Parentesis, exponentes, multiplicación, división, adicción y substración
#Para hacer las raíces cuadradas, se pueden usar los exponentes ** divido la mitad (1/2) o 0.5.





#Ahora veremos como tal los operadores logicos y de comparacion
#Imaginemos que tenemos un estudiante que no trabaja, como lo expreso?
es_estudiante = True
trabaja = False

#Si nos planteamos: esta persona es estudiante y trabaja. Eso es un False, como lo comprobamos?
es_estudiante and trabaja
#la ejecucion es False




#AHORA, si decimos que esta persona es estudiante o trabaja Utilizaremos el operador or
es_estudiante or trabaja




#AHORA, tenemos el operador not que nos servirá para invertir el valor booleano
#Si yo digo not es_estudiante y el valor original de es_estudiante era True, cambiara a False
not es_estudiante
#Hasta aqui los operadores logicos






#Operadores de comparacion


#Primero veremos el operador de igualdad ==
#Como podemos saber que lo que hay dentro de las variables es igual? Con el operador de ==
numero1 = 5
numero2 = 5
numero1 == numero2

#El opuesto a el operador de igualdad es el operador, distinto !=
numero3 = 3
numero1 != numero3 #Imprime True

#Tambien estan los operadores de mayor o menor que
numero3 > numero1 #Imprime False


#Tambien estan los operadores de mayor igual o menor igual que >= <=
numero1 >= numero2 #Imprime True, porque ambos valores son iguales

