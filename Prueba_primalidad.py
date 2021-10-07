#Haremos un programa que nos diga si un numero es primo o no

# Ahora haremos el programa
# 1.	Nuevo archivo Prueba_primalidad.py
# 2.	Definimos nuestra función y el if … equals .. execute, como nuestras buenas prácticas dentro del documento.
# 3.	Dentro de nuestra función haremos una variable que tendrá como valor un numero entero, que introduciremos en un input.
# 4.	Luego tenemos que indicarle a la función la siguiente lógica si el numero es primo, entonces imprime ‘Es primo’. Sino, imprime ‘No es primo’
#       If es_primo(numero):
#              Print(‘Es primo’)
#       Else:
#             Print(‘No es primo’)
#       Notese que pusimos el if, sin poner una comparación, esto es porque es opcional colocar si un valor es True, de entrada siempre sera True, por lo que no tenemos que escribir if es_primo(numero) == True:, sino, de una vez se entiende la condicional.
# 5.	Lo siguiente es crear la función es_primo, la cual sabemos, recibe un numero como parámetro.
#            a.	Definiremos una variable contador que tendrá el valor 0
#            b.	Establecemos un ciclo en el que, para i en el rango que va de 1 hasta el numero que nos ingreso el usuario.
#            For i in range(1, numero + 1)
#            Recordemos que el + 1, es para que el bucle pueda avanzar hasta ese numero que nos dio el usuario.
#            Y dentro de este ciclo: si i es igual a 1 o i es igual a numero: nos saltamos la vuelta del ciclo con un continue
#            If i == 1 or i == numero:
#                               Continue
#            Y luego otra condicional: Si dividir el numero por i, nos da como resto 0: entonces vamos a sumarle un valor al contador.
#            If numero % i = 0:
#                     Contador += 1
#            c.	Luego de terminar nuestro ciclo, haremos una condicional que tenga esta lógica Si el contador, es igual a 0: entonces return verdadero True.
#            Sino return False. Y asi es como conectamos con nuestra función run() en su condicional
#            d.	Toda esta lógica finalmente nos dice: tenemos una variable disponible que ingresa un numero desde el usuario, luego definimos un contador y luego hacemos un ciclo en el que vamos a ir desde el 1 hasta el numero ingresado en input. En cada vuelta del ciclo afirmamos que si la variable i que representa a cada variable del ciclo, es igual a 1, o la variable i es igual al numero, entonces nos vamos a saltar esta vuelta del ciclo. Si no nos saltamos la vuelta del ciclo, preguntamos,  que si el resto de la división de numero por i, es igual a 0, aumentaremos un 1 al contador, es decir que el numero no es primo y seguimos. Luego viene la condición de que si contador 


def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()


#Reto: Encontrar una forma mas eficiente de hacer el codigo para saber si un numero es primo o no, a partir de las herramientas matematicas.