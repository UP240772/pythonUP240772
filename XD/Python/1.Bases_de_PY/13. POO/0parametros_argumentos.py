#parametro: es una variable que se usa en una funcion
#argumento: es el valor que toma esa variable

# def suma(num1,num2):
#     # num1 = 20
#     # num2 = 30
#     suma = num1 + num2 
#     return suma


# print(suma(30,20))
# print(suma(50,10))
# print(suma(30,40))

#aplicacion de parametros y argumentos 

# def sum(num1, num2): 
#     suma = num1 + num2
#     return suma 

# # print(sum(2,4))
# # print(sum(100, 50))
# # num1 = int(input('Ingrese el valor del numero 1: '))
# # num2 = int(input('Ingrese el valor del numero 2: '))
# # print(sum(num1, num2))

# #variables globales
# # funcion estatica  
def valores(): 
    global num1, num2
    num1 = 110
    num2 = 40
    res = num1 + num2 
    return res

print(valores())
print(num1)

# # estos valores no estan definidos fuera  de la funcion
# # global num1, num2
# resta = num1 - num2 
# print(resta)

# ahora ambas variables se hicieron globales, para poder ser utilizadas tanto como dentro como fuera de la funcion
# def valores(): 
#     global num1, num2 #global es una palabra reservada para hacer que una variable YA DECLARADA sea global
#     # esto es incorrecto
#     # global num = 140
#     num1 = 110
#     num2 = 40
#     res = num1 + num2 
#     return res

# print(valores())

# resta = num1 - num2 
# print(resta)

# Argumentos indefinidos 

# se usan cuando no se sabe la cantidad de datos que se van a ingresar a la funcion o codigo a utilizar 
#  ejemplo
# def argumento(num):
#     return(type(num))

# print(argumento(10)) 
# print(argumento(22.44))
# print(argumento('cadena'))

# cuando queremos ingresar varios datos a la vez se pone un * como prefijo del parametro en la funcion

# def argumento(*num): #al poner el asterisco ahora los datos que le mandemos los almacenara en una tupla 
#     return(type(num))

# print(argumento(10)) 
# # se pueden hacer asignaciones multiples 
# print(argumento(10, 30, 40, 50, 60, 'tupla')) 

# def argumento(*num):
#     for i in num: #con un for podemos recorrer los lugares de la tupla 
#         print(i)


# print(argumento(10, 30, 40, 50, 60, 'tupla'))

#EJERCICIOS 

# 1 
# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con 
# argumentos de base y altura; y la otra el area de un circulo con argumento de radio






# def cuadrado(base, altura): 
#     res = base * altura
#     return res

# def circulo(radio):
#     area = 3.14 * radio ** 2
#     return area


# decicion = input('Presione "R" si desea calcular el area de un rectangulo, presione "C" si desea calcular el area de un circulo: ')
# if decicion.capitalize() == 'R': 
#     base = float(input('Ingrese la base del rectangulo: '))
#     altura = float(input('Ingrese la altura del rectangulo: '))
#     print('El area del rectangulo es: ', cuadrado(base, altura))

# elif decicion.capitalize() == 'C': 
#     radio = float(input('Ingrese el radio del circulo: '))
#     print('El area del circulo es: ', circulo(radio))

# else: 
#     print('Ha tecleado incorrectamente, intente de nuevo ')

# 2
# Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

# def medida(*num): 
#     # print(len(num))
#     return len(num)

# print(medida(1,2,3,4,5))
