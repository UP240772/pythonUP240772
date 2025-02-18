# ejercicio 1
# Crear un programa que tenga la variable con la cadena 'te quiero solo como amigo'
# y muestre la siguiente informacion:





cadena = 'te quiero solo como amigo'
# imprima los dos primeros caracteres
print(cadena[0 : 2])

# los tres ultimos caracteres
#print(len(cadena))
print(cadena[(len(cadena))-3 : ])
print(cadena[-3 : ])

# imprima dicha cadena cada dos caracteres
print(cadena[: :2]) #el tercer parametro es el paso con el que imprime lso espacios del string

# dicha cadena en sentido inverso
print(cadena[: : -1]) #paso 1 en inverso

# imprima la cadena en un sentido y luego en sentido inverso
print(cadena + cadena[: : -1])

# ejercicio 2
# crear un programa que tenga una variable con la cadena 'separado' e inserte el caracter ',' entre cada letra de la cadena.


palabra = 'separado'
print(palabra)
reemplazo = palabra.replace('', ',') #reemplaza el espacio entre cada letra por una coma 
print(reemplazo)


cadena = 'uso del metodo replace' #reemplaza posiciones de una cadena por otro parametro
cadena2 = cadena.replace('e', 'E') #reemplaza e por E
print(cadena2)

