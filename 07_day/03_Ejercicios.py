#NIVEL 3

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
st = set(age)
print(st)
LongitudSt = len(st)
LongitudAges = len(age)
st.difference(age)

#Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto
print("La cadena es una secuencia de caracteres")
print("La lista es una coleccion ordenada y mutable de elementos")
print("La tupla es una coleccion de elementos ordenada, similar a una lista, pero es inmutable")
print("El set es una coleccion desordenada de elementos unicos")

#¿Cuántas palabras únicas se han utilizado en la oración? Utilice los métodos de división y de configuración para obtener las palabras únicas.
##Soy profesor y me encanta inspirar y enseñar a la gente
