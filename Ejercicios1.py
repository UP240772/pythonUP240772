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

#Calcular pendiente (m)
y2, y1 = punto2[1], punto1[1]
x2, x1 = punto2[0], punto1[0]
pendiente = (y2 - y1) / (x2 - x1)

#Calcular la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Pendiente: ", pendiente)
print("Distancia euclidiana:", distancia)

# Definir las palabras
palabra1 = 'python'
palabra2 = 'dragon'

# Encontrar la longitud de cada palabra
longitud1 = len(palabra1)
longitud2 = len(palabra2)

# Hacer una afirmación de comparación falsa
afirmacion_falsa = longitud1 > longitud2  # Aquí hacemos una afirmación falsa

print(f"Longitud de 'python': {longitud1}")
print(f"Longitud de 'dragon': {longitud2}")
print(f"Afirmación falsa (python es más largo que dragon): {afirmacion_falsa}")

# Definir las palabras
palabra1 = 'python'
palabra2 = 'dragon'
# Comprobar si 'on' se encuentra en ambas palabras
subcadena = 'on'
resultado = (subcadena in palabra1) and (subcadena in palabra2)
print(f"¿La subcadena '{subcadena}' se encuentra en ambas palabras? {resultado}")

def contiene_jerga(oracion, jerga):
    # Dividir la oración en palabras
    palabras = oracion.lower().split()
    
    # Comprobar si alguna palabra de jerga está en la oración
    for palabra in jerga:
        if palabra.lower() in palabras:
            return True
    return False

# Lista de palabras de jerga
lista_jerga = ['jerga', 'otra_palabra_de_jerga', 'mas_palabras']

# Oración a comprobar
oracion = 'Espero que este curso no esté lleno de jerga.'

# Verificar si contiene jerga
resultado = contiene_jerga(oracion, lista_jerga)
print("¿La oración contiene jerga?", resultado)

palabra1 = 'dragon'
palabra2 = 'python'
subcadena = 'on'

# Verificar si la subcadena está en ambas palabras
presente_en_ambas = subcadena in palabra1 and subcadena in palabra2

print(f'¿La subcadena "{subcadena}" está en ambas palabras? {presente_en_ambas}')

# Texto
texto = 'Python'

# Encontrar la longitud del texto
longitud = len(texto)

# Convertir la longitud a flotante
longitud_flotante = float(longitud)

# Convertir el valor flotante a cadena
longitud_cadena = str(longitud_flotante)

# Imprimir el resultado
print(f'Longitud del texto: {longitud}')
print(f'Longitud como flotante: {longitud_flotante}')
print(f'Longitud como cadena: {longitud_cadena}')

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Ejemplo de uso
numero = 10
if es_par(numero):
    print(f'{numero} es un número par.')
else:
    print(f'{numero} es un número impar.')

#DIVISION DEL PISO 7 POR 3

ResultadoDivision = 7 // 3
ValorEntero = int(2.7)
SonIguales = ResultadoDivision == ValorEntero
print(float("¿La division es igual al valor entero convertido de 2.7", SonIguales))
#DIA 4
