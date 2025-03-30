#Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.
suma = 0
for numero in range(101):
    suma += numero
    print("La suma de todos los numeros es : ", suma)

#Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todos los impares.
SumaPares = 0
SumaImpares = 0
for numero in range(101):
    if numero % 2 == 0:
        SumaPares += numero
    else:
        numero % 3 == 0
        SumaImpares += numero
print("La suma de todos los pares es: ", SumaPares)
print("La suma de todos los impares es: ", SumaImpares)