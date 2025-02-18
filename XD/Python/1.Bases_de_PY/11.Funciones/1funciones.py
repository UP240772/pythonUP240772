#funcion: secuencia de sentencias que realizan una operacion
#parametro: variables que se definen al declarar funciones, se usan para enviar valores al llamar a la funcion
#argumento: valor que toma cada parametro dentro de la funcion 

#funciones en py

# num = '70'
# lista = [12,60,70,1,-2]
# print(type(num)) #type es una funcion propia de py, asi como print
# print(len(lista))#len es una funcionque retorna el tamaño de la lista
# print(max(lista))#max devuelve el valor maximo de la lista
# print(min(lista))#min devuelve el valor minimo en la lista

# sintaxis de una funcion
# def <nombre de la funcion>():
#     <sentencias>


def funcion1():
    print('algo')
    print('un mensaje')

# def saludo(): 
#     print('Hola alumnos ')
#     print('Sentencia 2')

# #como se manda llamar una funcion 
# saludo()
# saludo()
funcion1()

def tabla7():
    for i in range(1, 11): 
        print('7 x {} = {}'.format(i, i*7))

tabla7()
# print('--------------------------------------------------')
# tabla7()

#EJERCICIO 1 
# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir 
# numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen 
# los numeros pares e impares dentro de dos listas nuevas

# lista = []
# num = 0

# def pedir(): 
#     i = 0
#     while i <= 5: 
#         num = int(input('Ingresa un numero: ')) 
#         lista.append(num)
#         i += 1

# # pedir()
# # print(lista)

# def ordenar(): 
#     lista.sort()
#     pares = []
#     impares = []
#     for i in lista: 
#         if i % 2 == 0: 
#             pares.append(i)
#         else: 
#             impares.append(i)
#     print(pares)
#     print(impares)

# pedir()
# ordenar()



# EJERCICIO 2
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

#forma 1

# def factorial():
#     num = int(input('Ingrese un numero entero positivo: '))
#     if num > 0: 
#         factorial = 1
#         for i in range(1, num+1):
#             factorial = factorial * i
#         print(factorial) 
        
#     else: 
#         print('Te dije positivo :v ')

# factorial()

#forma 2


def factorial():
    from math import factorial
    num = int(input('Ingrese un numero entero positivo: '))
    if num > 0: 
        print(factorial(num))
    else: 
        print('Te dije positivo ')

factorial()


