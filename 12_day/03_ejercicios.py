#Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#Escriba una función que devuelva un array de siete números aleatorios en un rango del 0 al 9. Todos los números deben ser únicos
def seven_random():
    s = set()
    lst = []
    while True:
        if len(s) == 7:
            lst = s
            return lst
        n = random.randint(0, 10)
        s.add(n)

#No hay salida de nada