#sintaxis de diccionarios 

# diccionario = {'Usuario' : "JGarcia", 'Contrasena' : 12345} #se componen de una clave y un valor 
# print(type(diccionario))
#no se pueden repetir dos claves 
diccionario2 = {'diccionario' : "conjunto de datos", 'Apellido' : "Garcia", 'Estatura' : 1.7, 12 : "edad"}
# print(diccionario2)
# print(diccionario2.keys()) #imprime solo las claves 
# print(diccionario2.values()) #imprime solo los valores

print(diccionario2["Estatura"]) #mandar llamar una clave, imprime el valor de la clave
diccionario2["Peso"] = 70 #agrega una definicion al diccionario 
print(diccionario2)
diccionario2["Nombre"] = "Juan" #cambiar un valor 
print(diccionario2)
