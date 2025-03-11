##DIA 6

#Crear una tupla vacía
TuplaVacia = ()

#Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
Hermana = ("Mayeli")
Hermano = ("Darell")
print(Hermana)
print(Hermano)

#Unir tuplas de hermanos y hermanas y asignarlas a hermanos

Hermanos = (Hermano + " " + Hermana)
print(Hermanos)

#¿Cuántos hermanos tienes?
Hermanos = ("Darell", "Mayeli")
Contador = len(Hermanos)
print(Contador)

#Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members
Hermanos = ("Darell", "Mayeli")
Padres = ("Sagit", "Lizeth")
MiembrosDeFamilia = (Hermanos+Padres)
print(MiembrosDeFamilia)

##NIVEL 2

#Desempaquetar hermanos y padres de family_members
MiembrosDeFamilia
Papás = MiembrosDeFamilia [2:4]
Camaradas = MiembrosDeFamilia [0:2]
print(Papás)
print(Camaradas)

#Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
Frutas = ("Manzana", "Pera", "Melon", "Sandia")
Verduras = ("Zanahoria", "Calabaza", "Tomate", "Jitomate")
ProductosAnimales = ("Leche", "Queso", "Carne", "Seso")
food_stuff_tp = (Frutas + Verduras + ProductosAnimales)
print (food_stuff_tp)

#Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = (Frutas + Verduras + ProductosAnimales)
print(food_stuff_lt)

#Extraiga el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
food_stuff_lt = ('Manzana', 'Pera', 'Melon', 'Sandia', 'Zanahoria', 'Calabaza', 'Tomate', 'Jitomate', 'Leche', 'Queso', 'Carne', 'Seso')
PrimerElemento = food_stuff_lt [5]
SegundoElemento = food_stuff_lt [6]
print(PrimerElemento)
print(SegundoElemento)

#Separa los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
Separo1 = food_stuff_lt [0:2]
Separo2 = food_stuff_lt [9:11]
print(Separo1)
print(Separo2)

# Eliminar la tupla food_staff_tp por completo
del food_stuff_tp

#Comprueba si un elemento existe en una tupla:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
##Comprueba si 'Estonia' es un país nórdico
print("Estonia" in nordic_countries)
##Comprueba si 'Islandia' es un país nórdico
print("Islandia" in nordic_countries)

##FIN