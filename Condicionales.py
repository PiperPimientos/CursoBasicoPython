#Condicionales
#haremos un programa para entenderlas
edad = int(input("Escribe tu edad:"))
if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
#Estructura clasica if else

#Otro ejemplo pero con elif
numero = int(input("Escribe un numero: "))
if numero > 5:
    print("Es mayor a 5")
elif numero == 5:
    print("Es igual a 5")
else:
    print("Es menor a 5")
#Podemos hacer cuantos elif necesitemos para validar una condicion