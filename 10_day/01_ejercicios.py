#Itere del 0 al 10 usando el bucle for, haga lo mismo usando el bucle while.
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numeros:
    print(number)

contar = 0
while contar < 11:
    print(contar)
    contar = contar + 1

#Itere de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.
Numero = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in Numero:
    print(number)

contar = 10
while contar >= 0:
    print(contar)
    contar = contar - 1

#Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
for i in range(8):
    print('# ' * i)

#Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
gato = "# "
for i in range(4):
    print(gato * i)

#Imprima el siguiente patrón:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

i = 0
contar = 0
while contar < 11:
    mult = i*i
    print(i, "x", i, mult)
    i = i + 1
    contar = contar + 1

#Itere a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprima los elementos.
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for iterator in lista:
    print(lista)

#Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares
conteo = 0
while conteo < 101:
    print(conteo)
    conteo = conteo + 2

#Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares
conteo = 0
num = 0
while conteo < 101:
    print(conteo)
    if num % 2 == 0:
        pass
    else:
        print(num)
