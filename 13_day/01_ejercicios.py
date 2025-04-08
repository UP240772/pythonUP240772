#Filtrar solo los negativos y ceros en la lista usando la comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([n for n in numbers if n < 0])

#Aplana la siguiente lista de listas de listas a una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([n for row in list_of_lists for inner in row for n in inner])

#Usando la comprensión de listas, cree la siguiente lista de tuplas:
print([(n, 1, n, n*n, n*n*n, n*n*n*n, n*n*n*n*n) for n in range(0, 11)])

#Aplana la siguiente lista a una nueva lista:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([country.upper()
       for row in countries for tup in row for country in tup])

#Cambie la siguiente lista a una lista de diccionarios:
#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
tups = [tup for row in countries for tup in row]
lst = []
for i in tups:
    d = {}
    d['country'] = i[0]
    d['city'] = i[1]
    lst.append(d)
print(lst)

#Cambie la siguiente lista de listas a una lista de cadenas concatenadas:
names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([name for row in names for tup in row for name in tup])

#Escriba una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales.
def m(x1, y1, x2, y2): return (y2-y1)/(x2-x1)
print(m(2, 2, 4, 8))

print("revisado")