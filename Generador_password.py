#Proyecto Final, generador de contrasenas

# Haremos un generador automático de contraseñas. Esto es una funcionalidad que tiene Firefox, de rellenarnos el campo de contraseñas con una contraseña aleatoria y segura que despues se guarda en la DB del mismo navegador.

# 1.	importaremos el modulo random
# 2.	Creamos la base de nuestro código con buenas practicas
# 3.	Dentro de nuestra función definiremos que la variable password = gen_password() esta función que definimos dentro de la variable password, que nos servirá para generar aleatoriamente la contraseña
# 4.	Ahora haremos el print principal que nos diga (‘Tu nuevo password es: ‘) y le concatenamos password
# print(‘Tu nuevo password es: ‘ + password)
# 5.	Ahora definiremos nuestra función gen_password() antes de nuestra función run(), lógicamente, para conservar el orden
#       a.	No recibirá parámetros ()
#       b.	Generaremos 4 listas de caracteres que generaremos. Estos serán, letras en mayuscula, letras en minúscula, numeros y símbolos.
#       MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
#       MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
#       NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#       CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
#       Notese que las pondremos como constantes, su letra de identificador esta en mayuscula.
#       c.	Lo que haremos ahora es sumar todas estas listas en una lista única, llamada caracteres = MAYUS + MINUS + NUMS + CHARS
#       d.	Ahora tendremos que definir que nuestra variable password va ser igual a una lista, con una generación al azar de la contraseña a partir de todos los caracteres que creamos. Hasta llenar 15 caracteres.
#       password = [ ]
#       e.	Luego generaremos un ciclo for, en el que tendremos la lógica para i en el rango de la cantidad de vueltas que de el ciclo para elegir un carácter, que será de 15: 
#       for i in range(15)
#       f.	y adentro generamos una nueva variable carácter_random que tendrá el valor de random.choice(caracteres) con este método .choice(), que es una función especial del método random, lo que haremos.
#       Luego en esta misma lista password vamos a sacar un .append(carácter_random) para meter ese carácter dentro de la lista password = [ ]
    
#       Es decir, vamos a tener un ciclo que va tener 15 vueltas, se genera una variable llamada carácter_random que va a tener un carácter de nuestra lista caracteres, que será al azar y vamos a meter ese carácter, dentro de nuestra lista password.
#       g.	Finalmente tendremos que convertir esta lista password a un string. Convertimos ese tipo de dato con un método llamado ‘ ‘.join() y dentro de los paréntesis, esa lista que queremos convertir que es password
#       Con esto generamos un string de mi lista original
#       h.	Ahora lo ultimo que resta es hacer un return de password, para que en nuestra función run(), al ejecutar la función gen_password() la misma se guarde dentro de la variable password.


import random

def gen_password():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = "".join(password)
    return password

def run():
    password = gen_password()
    print('Tu nuevo password es: ' + password)

if __name__ == '__main__':
    run() 

    #FIN DEL CURSO