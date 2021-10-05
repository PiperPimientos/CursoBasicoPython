#Crearemos un programa que identifica si la palabra que ingresamos es un palindromo o no

# 1.	Crearemos una función principal, que es la que va correr el programa al principio. Es una buena práctica en Python tener una función que es la que va correr el programa al principio. Nuestra función tendrá como nombre run, por lo tanto debe quedar asi, def run()
# 2.	Para crear la condicional lo haremos utilizando los dos guiones bajos al llamar la variable, que seria como: if __name__ == ‘__main__’: 
# 3.	Vamos a invocar la función run dentro de esa condicional,
# 4.	Dentro de la función run, vamos a guardar una variable que va tener como nombre palabra y como valor input(‘Escribe una palabra: ‘)
# 5.	Ahora tendremos que definir si esa palabra es palíndromo o no, para saberlo usaremos los booleanos, pero primero tendremos que llamar una función propia que lo haga, por eso dejaremos como valor la invocación de la función palíndromo es_palindromo = palíndromo(palabra) que si lo notamos, tendrá como parámetro, el input palabra
# 6.	Luego construiremos esa condicional que estará sujeta a si es_palindromo es true o es false.
# 7.	Ahora crearemos la función palíndromo y recordemos que siempre se debe construir por encima de la línea en la que la invocamos, por lo tanto quedara por encima de la función run. Def palíndromo() que como parámetro va recibir el input palabra. Ahora vamos a construir esa lógica
#    a.	Primero tenemos que quitar los espacios, esto es, si por ejemplo tenemos palabras como “luz azul” en donde tendremos un espacio que al ejecutar no nos permitirá identificar si es un palidromo, asi que utilizamos el método .replace que nos servirá para modificar la variable palabra, palabra = palabra.replace() y dentro vamos a separar todos los espacios por un string vacio, sin espacios (‘  ‘, ‘’) reemplazando todos los caracteres espacio, por la nada.
#    b.	Ahora utilizando el método .lower pasaremos la palabra a minúsculas para que cuando el programa se ejecute, todas las letras sean iguales en ambos sentidos. Palabra = palabra.lower()
#    c.	Lo siguiente es crear esa variable que contenga a la palabra invertida y tendra como nombre palabra_invertida guardando como valor el slices para palabra invertida palabra[::-1]
#    d.	Ahora para validar que la palabra invertida sea igual que la palabra, tendremos que crear una condicional if palabra == palabra_invertida: return True, es decir que la funcion va devolver verdadero, si no son iguales else return False

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()