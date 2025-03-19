#Ejercicios: Nivel 2
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordena la lista y encuentra la edad mínima y máxima.
edades.sort()
print(edades)

#Agregue la edad mínima y la edad máxima nuevamente a la lista
edades.insert(0, "19")
print(edades)
edades.insert(10, "26")

#Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Media=len(ages)//2
print(Media)
print("Punto 4")
#Find the average age (sum of all items divided by their number )
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Promedio=sum(ages)/len(ages)#La operacion sum() me sirve para sumar toda una cadena o lista sin tener que haser laoperacion de uno por uno 
print(Promedio)
print("Punto 5")
#Find the range of the ages (max minus min)
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=True)
print(ages)
print("Punto 6")
#Compare the value of (min - average) and (max - average), use abs() method
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
MinAge = (19 - Promedio)
MaxAge= (26 - Promedio)

print("Revisado")