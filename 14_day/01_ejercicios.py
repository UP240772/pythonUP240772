#Explique la diferencia entre mapa, filtro y reducción.
print("Mapa (map()) aplica una funcion dada a cada elemento de un iterable (como una lista o un conjunto) y devuelve un nuevo iterable con los resultados")
print("Filtro(filter()) selecciona lso elementos de un iterable que cumplen con una condicion dada y devuelve un nuevo iterable con los elementos seleccionados")
print("Reduccion(reduce()) aplica una funcion dada a los elementos de un iterable, de manera acumulativa, y devuelve un solo valor")

#Explique la diferencia entre función de orden superior, cierre y decorador.
print("Una funcion de orden superior es una funcion que acepta otra funcion como argumento o devuelve una funcion como resultado")
print("Un ciere es una funcion que tiene acceso a su entorno léxico, es decir, puede acceder a las variables de la funcion exterior incluso despues de que la funcion exterior haya terminado de ejecutarse")
print("Un decorador es una funcion de orden superior que se utiliza para modificar el comportamiento de otra funcion sin cambiar su implementacion. Un decorador es una forma de envolver una funcion con otra funcion")

#Defina una función de llamada antes de map, filter o reduce, vea los ejemplos.
numeros = [1,2,3,4,5]
def cuadrado(x):
    return x ** 2
NumerosCuadrados = map(cuadrado, numeros)
print(list(NumerosCuadrados))

#Utilice el bucle for para imprimir cada país en la lista de países.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

#Utilice for para imprimir cada nombre en la lista de nombres.
for name in names:
    print(name)

#Utilice for para imprimir cada número en la lista de números.

for number in numbers:
    print(number)
