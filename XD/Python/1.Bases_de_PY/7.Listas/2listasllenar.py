lista = [1,2,3] 
lista2 = [4,5,6]

# # #sumar una lista

lista3 = lista + lista2
print(lista3)
#no todos los operadores aritmeticos funcionan 
#no es concatenar

#concatenar

print('Esta es una lista de distintos datos: ', lista)

lista4 = [] #declaracion de una lista vacia
# print(type(lista))

# #llenar una lista
while True: 

    edad = int(input('Ingresa tu edad: '))
    lista4.append(edad)#el metodo append ingresa el dato al final de la lista
    print(lista4)

