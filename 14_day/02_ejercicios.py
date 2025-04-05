from functools import reduce
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
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = reduce(
    lambda x, y: x + y,map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(resultado)
#Declare una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
def get_string_lists(lst):
    new = []
    for item in lst:
        if type(item) == str:
            new.append(item)
    return new


print(get_string_lists([1, 2, 3, 4, 5, 7, 'hllo']))

#Utilice reducir para sumar todos los números en la lista de números.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def addNumbers (x,y):
    return int(x) + int (y)
total = reduce(addNumbers,numbers)
print(total)

#Utilice reduce para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def paisOracion (x,y):
    return x + ', ' + y
oracion = reduce(paisOracion,countries)
oracion1 = oracion + 'son paises de europa'
print(oracion1)

#Declare una función llamada categorize_countries que devuelva una lista de países con algún patrón común (puede encontrar la lista de países en este repositorio como Countries.js (por ejemplo, 'land', 'ia', 'island', 'stan')).
from countries import countries
def categorizeCountries (countries,pattern):
    return list(filter(lambda country: pattern in country.lower(),countries))
print(categorizeCountries(countries,'land'))

#Crea una función que devuelva un diccionario, donde las claves representan las letras iniciales de los países y los valores son la cantidad de nombres de países que comienzan con esa letra.
def countCountriesByInitial(countries):
    return dict(map(lambda letter: (letter, sum(1 for country in countries if country.startswith(letter))), sorted(set(map(lambda x: x[0], countries)))))
print(countCountriesByInitial(countries))

#Declare una función get_first_ten_countries: devuelve una lista de los primeros diez países de la lista Countries.js en la carpeta de datos.
def firsTen (countries):
    return list(map(lambda x:x, countries[:10]))
print(firsTen(countries))

#Declare una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.
def LastTen (countries):
    return list(map(lambda x:x, countries[-10:]))
print(LastTen(countries))
