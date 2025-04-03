#Declare la función add_two_numbers . Esta función acepta dos parámetros y devuelve una suma.
def add_two_numbers(a, b):
    return a+b  
print(add_two_numbers(1,2))

#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .
def area_of_circle(r):
    return 3.14*r*r
print(area_of_circle(5))

#Escriba una función llamada add_all_nums que tome cualquier número de argumentos y los sume. Compruebe si todos los elementos de la lista son de tipo numérico. De no ser así, proporcione una respuesta razonable.
def add_all_nums(*args):
    sum = 0
    for i in args:
        try:
            int(i)
            sum += i
        except:
            return "Only Int"
    return sum
print(add_all_nums(1, 2, 3, 4))

#La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
def convert_celcius_to_farenheit(c):
    return (c * (9/5)) + 32
print(convert_celcius_to_farenheit(0))

#Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano
def ChecarTemporada(Mes):
    if Mes in ["Septiembre", "Octubre", "Noviembre"]:
        print("Otoño")
    elif Mes in ["Diciembre", "Enero", "Febrero"]:
        print("Invierno")
    elif Mes in ["Marzo", "Abril", "Mayo"]:
        print("Primavera")
    elif Mes in ["Junio", "Julio", "Agosto"]:
        print("Verano")
    else:
        print("Ingresa el mes correctamente")
ChecarTemporada("Junio")

#Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal
def calculate_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

#La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escriba una función que calcule el conjunto solución de una ecuación cuadrática, solve_quadratic_eqn .
def solve_quadratic_eqn(a, b, c):
    sol1 = (-(b) + ((b)**2 - 4*a*c)**0.5)/(2*a)
    sol2 = (-(b) - ((b)**2 - 4*a*c)**0.5)/(2*a)
    print(f"Sol1 : {sol1}")
    print(f"Sol2 : {sol2}")

#Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.
def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 6, 8, 3])

#Declare una función llamada reverse_list. Esta recibe un array como parámetro y devuelve su valor inverso (usando bucles).
def reverse_list(lst):
    new_lst = []
    for i in range(-1, -(len(lst))-1, -1):
        new_lst.append(lst[i])
    return new_lst
print(reverse_list([1, 2, 3, 4]))

#Declare una función llamada capitalize_list_items. Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas.
def capitalize_list_items(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.capitalize())
    return new_lst
print(capitalize_list_items(['hello', 'world']))

#Declara una función llamada add_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento añadido al final.
def add_item(lst, item):
    lst.append(item)
    return lst
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#Declara una función llamada remove_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento eliminado.
def remove_item(lst, item):
    lst.remove(item)
    return lst


numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#Declara una función llamada suma_de_números. Esta función toma un parámetro numérico y suma todos los números en ese rango.
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        sum += i
    return sum


print(sum_of_numbers(5))

#Declara una función llamada suma_de_impares. Esta función toma un parámetro numérico y suma todos los números impares en ese rango.
def sum_of_odds(r):
    sum = 0
    for i in range(r+1):
        if i % 2 != 0:
            sum += i
    return sum

#Declara una función llamada suma_de_números_pares. Esta función toma un parámetro numérico y suma todos los números pares en ese rango.
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        if i % 2 == 0:
            sum += i
    return sum

print("revisado")