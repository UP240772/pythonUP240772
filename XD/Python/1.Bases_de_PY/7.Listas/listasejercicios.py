'''
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, 
debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''

lista = [20, 50, "Curso", 'Python', 3.14]
print('Estos son los valores actuales de la lista: ', lista)
d1 = input('Ingresa un numero: ')
d2 = input('Ingresa el segundo valor: ')

lista[0] = d1
lista[1] = d2

print('Esta es la lista con los datos cambiados: ', lista)

