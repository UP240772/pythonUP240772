#Declara tu edad como variable entera
miEdad = 18

#Declara tu altura como una variable flotante
miAltura = 1.72

#Declara una variable que almacene un numero complejo
z = 4 +3j

#Escribe un scrip que solicite al usuario ingresar la base y altura del triangulo y calcular el area de este triangulo
base = float(input("Ingrese la longitud de la base: "))
altura = float(input("Ingrese la altura del triangulo: "))
area = 0.5 * base * altura
print("El area del triangulo es de: ", area)

#Perimetro de un triangulo
ladoUno = float(input("Ingrese la longitud del lado 1: "))
ladoDos = float(input("Ingrese la longitud del lado 2: "))
ladoTres = float(input("Ingrese la longitud del lado 3: "))
perimetro = ladoUno + ladoDos + ladoTres
print("El perimetro del triangulo es de: ", perimetro)

#Calcular la longitud y el ancho de un rectangulo mediante un comando. Calcular su area
longitud = float(input("Ingrese la longitud del rectangulo: "))
ancho = float(input("Ingrese el ancho del triangulo: "))
area = longitud * ancho
perimetroRectangulo = 2 * (longitud + ancho)

#Radio de un circulo
radio = float(input("Ingrese la radio del circulo"))
areaDelCirculo = 3,14 * radio **2
Circunferencia = 2 * 3,14 * radio

# Definir la ecuación
def calcular_pendiente_intersecciones():
    # La ecuación es y = mx + b, donde m es la pendiente y b es la intersección con el eje y
    m = 2  # Pendiente
    b = -2  # Intersección con el eje y

    # La intersección con el eje x ocurre cuando y = 0
    # 0 = 2x - 2 => x = b / m
    x_interseccion = -b / m

    print(f"Pendiente (m): {m}")
    print(f"Intersección con el eje y (b): {b}")
    print(f"Intersección con el eje x: {x_interseccion}")

# Llamar a la función
calcular_pendiente_intersecciones()

import math

# Definir los puntos
punto1 = (2, 2)
punto2 = (6, 10)

Calcular la pendiente (m)
y2, y1 = punto2[1], punto1[1]
x2, x1 = punto2[0], punto1[0]
pendiente = (y2 - y1) / (x2 - x1)

#Calcular la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Pendiente: {pendiente}")
print(f"Distancia euclidiana: {distancia}")