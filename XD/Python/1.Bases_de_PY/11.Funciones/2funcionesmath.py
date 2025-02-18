# funciones matematicas propias de py
#librerias: conjunto de funciones que se pueden mandar a llamar, para usarlas hay que importarlas
# import math

# print(math.pow(10, 2))#pow eleva un numero a un exponente, en este caso 10 a la potencia 2 
# #pow funciona sin math pero en enteros 
# print(math.sqrt(64))#calcula la raiz cuadrada de un numero, en este caso 64, lo calcula en flotante
# print(math.issqrt(64)) #calcula la raiz en numeros enteros
# print(math.sin(90)) #calcula el seno
# print(math.cos(90)) # calcula el coseno de 90
# print(math.tan(90)) #calcula la tangente 
# print(math.factorial(10)) #calcula el factorial 

# import random #proporciona metodos random

# print(random.randint(1, 100)) #devuelve un numero aleatorio entre cierto rango que le mandemos, en este caso del 1 al 100 

#retorno de funciones 

# def <nombre de la funcion>(): 
#     <sentencias>
#     return # el return retorna un valor de la funcion
# def entero(): 
#     print('Este es un valor entero: ')
#     return 10 

# def decimal(): 
#     print('Este es un dato decimal: ')
#     return 9.99


# def frase():
#     return 'Soy Batman '


# frase()
# print(frase())

# decimal()
# print(decimal())

# entero()
# print(entero())

#retorno de variables

# def asignacion(): 
#     return 1,2,3,4,5 #se pueden incorporar a una variable 

# a,b,c,d,e = asignacion() #se iguala a la funcion

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#EJERCICIOS
#1
# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
# el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, 
# debe retornar 0

# def funcion():
#     num1 = float(input('Ingrese el primer numero: '))
#     num2 = float(input('Ingrese el segundo numero: '))
#     if num1 > num2: 
#         return 1
#     elif num2 > num1: 
#         return -1
#     else: 
#         return 0

# print(funcion())

#EJERCICIO 2 

# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 21%.

# def total():
#     monto = float(input('Ingresa el valor del producto que se esta pagando: '))
#     iva = int(input('Ingresa el valor del IVA: '))
#     if iva != 0:
#         if iva > 0: 
#             total = ((monto * iva) / 100) + monto 
#             return total 
#         else: 
#             return'El iva es negativo, no procede '

#     else: 
#         total = (monto * 0.21) + monto
#         return total 

# print('El total de su monto es: ', total())






