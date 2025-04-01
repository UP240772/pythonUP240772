#Declare la función add_two_numbers . Esta función acepta dos parámetros y devuelve una suma.
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .
def AreaCirculo():
    pi = 3.1416
    radio = 5
    area = pi * radio * radio
    print(area)
print(AreaCirculo())

#Escriba una función llamada add_all_nums que tome cualquier número de argumentos y los sume. Compruebe si todos los elementos de la lista son de tipo numérico. De no ser así, proporcione una respuesta razonable.
def add_all_nums (*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: '{arg}' no es un número. Por favor, proporciona solo valores numéricos."
        total += arg
    return total

