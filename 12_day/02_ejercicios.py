#Escriba una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, af. Consulte la tarea 6 para ver ejemplos de salida).
import random
def list_of_hexa_colors():
    n = random.randint(0, 10)
    s = "0123456789abcdef"
    lst = []
    for i in range(n):
        res = '#'
        for j in range(6):
            res += random.choice(s)
        lst.append(res)
    return lst

#Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
def list_of_rgb_colors():
    n = random.randint(0, 10)
    lst = []
    for i in range(n):
        r = random.randint(0, 256)
        b = random.randint(0, 256)
        g = random.randint(0, 256)
        lst.append(f"rgb({r},{b},{g})")
    return lst

#Escriba una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o rgb.
def generate_colors(type, n):
    if type == 'hexa':
        s = "0123456789abcdef"
        lst = []
        for i in range(n):
            res = '#'
            for j in range(6):
                res += random.choice(s)
            lst.append(res)
        print(lst)
    elif type == 'rgb':
        lst = []
        for i in range(n):
            r = random.randint(0, 256)
            b = random.randint(0, 256)
            g = random.randint(0, 256)
            lst.append(f"rgb({r},{b},{g})")
        print(lst)
    else:
        print("Enter type correctly")

print("revisado")