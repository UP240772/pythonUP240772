#Itere del 0 al 10 usando el bucle for, haga lo mismo usando el bucle while.
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numeros:
    print(number)

contar = 0
while contar < 11:
    print(contar)
    contar = contar +1

#Itere de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.
Numero = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in Numero:
    print(number)

contar = 0
while contar > 11:
    print(contar)
    contar = contar - 1

#Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
for i in range(1, 8):
    print('#' * i)

#Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8, 8):
    print("#" * i)

