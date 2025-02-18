#bucle while
i = 0
while i < 10:
    i += 1
    print('Estoy iterando y estoy en el salto: {}'.format(i))



#cada iteracion es una vuelta en el bucle, el iterador es la variable que incrementa y 
# es de la que depende el numero de iteraciones o vueltas, en este caso i
#El iterador es de vital importancia debido a que si no tiene un limite el ciclo, se volvera infinito

#EJERCICIO
# Escribir un programa que pida un numero al usuario y muetsre las tablas de multiplicar de ese numero 
# i = 0
# num = float(input('Ingrese un numero para mostrar sus multiplos del 1 al 10: '))
# while i < 10: 
#     i += 1
#     res = num * i
#     print('El numero {} multiplicado por {} es: {}'.format(num, i, res))

# EJERCICIO 2 
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido desde 1 hasta 
# su edad

# i = 0
# edad = int(input('Ingrese su edad: '))
# while i < edad: 
#     i += 1 
#     hace = edad - i
#     print('Hace {} años cumplio {} años '.format(i, hace))

#Bucle for 

# generalmente se usan para recorrer listas

numeros = ['uno', 'dos', 'tres']
num = [1,2,3]
for i in num: 
    print (i)   

# nombres = ['Juan', 'Maria', 'Jose', 'Karla']
# for j in nombres: 
#     print('Feliz año nuevo ', j)

#Imprimir en pantalla los numeros del 1 al 10, 
# luego pedirle al usuario dos numeros y mostrar el rango entre ambas cifras 

for i in range(1, 11):
    print(i)
#realmente el rango es de 1 hasta 9
tupla = 1,2,3,4,5
for i in tupla:
    print(i)



