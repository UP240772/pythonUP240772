diccionario = {1 : 2, 2 : 3, 3 : 4}
diccionario2 = {4 : 5, 6 : 7}
# print(diccionario)

# diccionario.pop(3) # el metodo pop recibe como parametro la clave que se desea eliminar y la elimina junto con su valor 
# print(diccionario)

# #metodo clear
# diccionario.clear() #limpia los datos del diccionario 
# print(diccionario)

# print(diccionario.get(2)) #recibe como parametro la llave y devuelve el valor anexado a la llave 

#agregar valores con metodos
diccionario.setdefault(4, 5) #recibe como parametros la clave y el valor separados por comas y lo agrega a la cola del diccionario
print(diccionario)

# #actualizar valor
diccionario.update(diccionario2) #recibe como paramtetro otro diccionario y lo agrega al original para crear uno solo 
print(diccionario)

diccionario.copy() #hace una copia del diccionario
print(diccionario) 