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
lado1 = float(input("Ingrese la longitud del lado 1: "))
lado2 = float(input("Ingrese la longitud del lado 2: "))
lado3 = float(input("Ingrese la longitud del lado 3: "))
perimetro = lado1 + lado2 + lado3
print("El perimetro del triangulo es de: ", perimetro)

#Calcular la longitud y el ancho de un rectangulo mediante un comando. Calcular su area
longitud = float(input("Ingrese la longitud del rectangulo: "))
ancho = float(input("Ingrese el ancho del triangulo: "))
area = longitud * ancho