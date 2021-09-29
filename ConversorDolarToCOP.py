#Ahora un convertidor de dolares a pesos colombianos
dolares = input("Cuantos dolares tienes? ")
dolares = float(dolares)
valor_peso = 0.00026
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " COP")