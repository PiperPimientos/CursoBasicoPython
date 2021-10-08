#Juego: Adivina el numero

# 1.	Vamos a crear un juego llamado adivina el numero.
# 2.	Las reglas son:
#        a.	La PC va pensar un numero aleatorio entre el 1 y el 100 y nosotros vamos a tener que adivinar que numero pensó la PC.
#        b.	Le vamos a decir como lógica: si nosotros acertamos la PC nos va decir que ganamos, o si fallamos, la PC nos va decir si el numero que dimos es mas grande o si por el contrario, es mas pequeño. Esto con la finalidad de encontrar el numero

import random

def run():
    numero_ganador = random.randint(0, 100)
    contador = int(input('Introduce un numero del 1 al 100 para jugar: '))
    while contador != numero_ganador:
        if contador  > numero_ganador:
            print('Es un numero mas pequeno')
        else:
            print('Es un numero mas grande')       
        contador = int(input('Introduce otro numero del 1 al 100: '))
    print('GANASTE!')    

if __name__ == '__main__':
    run()