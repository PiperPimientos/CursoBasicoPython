#Slices o rebanadas de strings
#Estructura variable_string[caracter_inicial : caracter_final : pasos]

# 1.	Creamos una variable llamada nombre que contenga como valor el string Felipe
# 2.	Si yo quiero obtener por ejemplo Fel, podríamos hacerlo con nombre[0:3] le decimos que queremos obtener todo lo que esta antes del índice 3. Por lo que nos devuelve el slice Fel. E incluso podríamos hacerlo simplemente con nombre[:3] y nos va seguir devolviendo Fel. O si queremos ir desde el índice 3 hasta el final nombre[3:] nos quedaría ‘lipe’
# 3.	Tambien podemos definir los slices por pasos de tanto en tanto, esto se hace con la siguiente sintaxis nombre[1:7:x] siendo x la cantidad de pasos que quiero dar entre cada slice, asi, por ejemplo si decimos nombre[0:4:2] nos saldría ‘lip’
# 4.	O si queremos decir que vamos desde el principio hasta el final, podemos hacerlo asi [::], igualmente con los pasos, que seria nombre[0::3], que es como decirle que vaya del principio hasta el final en pasos de 3 en 3
# 5.	En incluso podemos hacerlo en pasos inversos, es decir llamar los string pero desde el final hasta el principio, por ejemplo si le decimos que cree una slice desde el principio hasta el final, pero en pasos de 1 en 1 negativo, devuelve todo el string al reves nombre[::-1]
