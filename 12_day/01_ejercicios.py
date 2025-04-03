#Escriba una función que genere un random_user_id de seis dígitos/caracteres
import random
def random_user_id():
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    res = ''
    for i in range(6):
        res += random.choice(s)
    return res

#Modifique la tarea anterior. Declare una función llamada user_id_gen_by_user. No acepta parámetros, pero acepta dos entradas mediante input(). Una de las entradas es el número de caracteres y la otra, el número de ID que se generarán.
def user_id_gen_by_user():
    n = int(input("Enter n : "))
    t = int(input("Enter t : "))
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(t):
        res = ''
        for j in range(n):
            res += random.choice(s)
        print(res)

#Escriba una función llamada rgb_color_gen. Esta generará colores RGB (tres valores de 0 a 255 cada uno).
def rgb_color_gen():
    r = random.randint(0, 256)
    b = random.randint(0, 256)
    g = random.randint(0, 256)
    return f"rgb({r},{b},{g})"

print("revisado")