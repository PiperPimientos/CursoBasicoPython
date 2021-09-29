#Este sera nuestro primer programa en el Curso Basico de Python

#cantidad de pesos colombianos que el usuario nos va ingresar
pesos = input("Cuantos pesos colombianos tienes? ")
#transformar ese input a un valor tipo float, para ello le reasignaremos el valor a la variable pesos
pesos = float(pesos)
#variable llamada valor_dolar y le asignaremos el valor de 3875 que es aproximadamente el valor que tiene un dólar hoy
valor_dolar = 3875
#necesitamos saber cuantos dolares tenemos, para ello creamos la variable dólares y le asignamos el valor de pesos dividido valor_dolar. 
dolares = pesos / valor_dolar
#Si queremos que no salgan mas que dos decimales
dolares = round(dolares, 2)
#convertir esos dólares a un texto, porque queremos imprimir en consola el valor de esos dólares pero en texto
dolares = str(dolares)
#solo falta el print 
print("Tienes $" + dolares + " dolares")

#Ejecutamos el codigo con el comando en la terminal: python3 ConversorMonedas.py