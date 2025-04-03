#Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))

#Utilice el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números
squares = map(lambda x: x*x, numbers)
print(list(squares))

#Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))

#Utilice el filtro para filtrar los países que contienen la palabra "tierra".
def is_land(s):
    if 'land' in s:
        return True
    else:
        return False
land = filter(is_land, countries)
print(list(land))

#Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.
def SeisLetras(s):
    if len(s) == 6:
        return True
    else:
        return False
Seis = filter(SeisLetras, countries)
print(list(Seis))

#Utilice el filtro para filtrar los países que comienzan con 'E'
def EmpiezaCon(s):
    if s[0] == "E":
        return True
    else: 
        return False
    
Empieza = filter(EmpiezaCon, countries)
print(list(Empieza))

#Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback)).

#Declare una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
def get_string_lists(lst):
    new = []
    for item in lst:
        if type(item) == str:
            new.append(item)
    return new


print(get_string_lists([1, 2, 3, 4, 5, 7, 'hllo']))
