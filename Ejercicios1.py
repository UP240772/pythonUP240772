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

import math

# Parte 1: Ecuación de la recta y = 2x - 2
m = 2  # Pendiente
interseccion_y = -2  # Intersección con el eje y
interseccion_x = -interseccion_y / m  # Intersección con el eje x

print(f'Pendiente: {m}')
print(f'Intersección con el eje y: {interseccion_y}')
print(f'Intersección con el eje x: {interseccion_x}')

# Parte 2: Calcular la pendiente y la distancia euclidiana entre (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calcular la pendiente
pendiente = (y2 - y1) / (x2 - x1)

# Calcular la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'Pendiente entre los puntos (2,2) y (6,10): {pendiente}')
print(f'Distancia euclidiana entre los puntos (2,2) y (6,10): {distancia}')

# Parte 3: Comparar las pendientes
pendiente_ecuacion = m
pendiente_puntos = pendiente

print(f'La pendiente de la ecuación y = 2x - 2 es {pendiente_ecuacion}')
print(f'La pendiente entre los puntos (2,2) y (6,10) es {pendiente_puntos}')

if pendiente_ecuacion == pendiente_puntos:
    print('Las pendientes son iguales.')
else:
    print('Las pendientes son diferentes.')

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

#Espero que este curso no esté lleno de jerga . Utilice el operador in para comprobar si hay jerga en la oración.
Frase = "Espero que este curso no esté lleno de jerga"
print ("Hay Jerga" in Frase) #True
print ("No hay jerga" in Frase) #False

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


# Definir las variables
cadena = '10'
entero = 10

# Comprobar si los tipos son iguales
tipos_iguales = type(cadena) == type(entero)

# Imprimir el resultado
print(f'¿El tipo de "10" es igual al tipo de 10? {tipos_iguales}')


#Comprueba si int(9.8) es igual a 10
Valor_Entero = int("9.81")
ValorEsperado = 10
EsIgual = Valor_Entero == ValorEsperado
print(float("¿El valor entero es igual a 10? ", EsIgual))


#Salario
HorasTrabajadas = float(input("Ingrese las horas trabajadas: "))
TarifaPorHora = float(input("Ingrese su tarifa por hora: "))
Salario = HorasTrabajadas * TarifaPorHora
print("Su salario es de: ", Salario)


#Segundos que puede vivir
Años = float(input("Ingrese la cantidad de años que ha vivido"))
Segundos = Años * 31,622,400 
print ("Usted ha vivido esta cantidad de segundos: ", Segundos)


#TABLA
# Imprimir la cabecera de la tabla
print('Número | n^0 | n^1 | n^2 | n^3')

# Generar y mostrar la tabla


#DIA 4
