lista = ['Python', 24, 'Jose', 'alex', 12]

# print(lista[3])
# lista[3] = 'Alex'
# print(lista[3])

#metodos
#metodos para eliminar elementos de una lista

lista.pop() #pop toma el ultimo elemento de la lista y lo elimina 
print(lista)

lista.remove(24)#remove elimina el dato que le mandemos como parametro
print(lista)

lista.remove(lista[3])#tambien funciona con posiciones de la lista
print(lista)

