# num = '70'
# lista = [12, 13, 14,15]

# #ejemplos de funciones propias del lenguaje
# # print(num)
# # print(type(lista))
# # print(len(lista))
# # print(max(lista))
# # print(min(lista))

# #sintaxis para declarar una funcion
# #funcion sin parametros y sin retorno de valores 
# def nombre_de_funcion(): 
#     print('Estoy utilizando funciones ')
# #funcion sin parametros y con retorno de valores 
# def suma():
#     a = int(input('Ingresa el primer valor'))
#     b = int(input('Ingresa el primer valor'))
#     res = a + b
#     return res
# #funcion con parametros pero con retorno de valor
# def parametros(a,b):
#     res = a**b
#     return res




# nombre_de_funcion()
# print(suma())
# print(parametros(12, 2))

# def tabladel7():
#     for i in range(1, 11): 
#         print('7 x {} = {}'.format(i, i+7))

# tabladel7()


# def openApps(app): 
#     print('Has abierto {}'.format(app))

# openApps('Facebook')
# openApps('Google')

def factorial():
    num = int(input('Ingrese un numero entero positivo: '))
    if num > 0: 
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        print(factorial) 
        
    else: 
        print('Te dije positivo ')

factorial()







