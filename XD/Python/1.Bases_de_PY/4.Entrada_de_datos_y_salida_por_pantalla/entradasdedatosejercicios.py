# Ejercicio 1

#Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula #general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el #proceso para que al final muestre el mensaje: “La solución es: <solucion>”
from math import sqrt

A = int(input('Ingresa el valor de A: '))
B = int(input('Ingresa el valor de B: '))
C = int(input('Ingresa el valor de C: '))
x1 = 0
x2 = 0

if ((B**2)-(4*A*C)) < 0:
    print('Raiz imaginaria ')
else: 
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print('La solucion es: \nx1=',x1, '\nx2=',x2)



# Ejercicio 2

# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado #curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
# Considere:
# PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
# Donde: P1, P2, P3 : Practicas
# PP: promedio de práctica
# PROM: promedio
# EP: examen parcial
# EF: examen final

practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingrese el valor de la practica 2: '))
practica3 = float(input('Ingrese el valor de la practica 3: '))
examenparcial = float(input('Ingrese el valor del examen parcial: '))
examenfinal = float(input('Ingrese el valor del examen final: '))
PP = (practica1 + practica2 + practica3) / 3
pf = (PP + 2 * examenparcial + 3 * examenfinal)/6
print('El promedio final del estudiante es de:\n ', pf)


