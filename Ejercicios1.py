#DIA 3  
#Area Triangulo
base = float(input("Ingrese la longitud de la base"))
altura = float(input("Ingrese la altura del triangulo"))
Area = 0.5 * base * altura 
print("el area del triangulo es de: ",Area)

#Peso de un objeto
mass = float(input("Ingrese la masa del objeto: "))
gravity = 9.81
weight = mass * gravity
print(weight, 'Kg')

#Area de un rectangulo
length = float(input("Ingrese la longitud: "))
width = float(input("Ingrese la altura: "))
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

#Calcular la densidad de un liquido 
mass = float(input("Ingrese la masa del liquido: ")) # in Kg
volume = float(input("Ingrese el volumen del liquido: ")) # in cubic meter
density = mass / volume # 1000 Kg/m^3
print("La densidad del liquido es: ", density)

#Area de un circulo
radius = float(input("Ingrese el radio del circulo"))                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)