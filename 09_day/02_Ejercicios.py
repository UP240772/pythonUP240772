#Escriba un código que califique a los estudiantes según sus puntuaciones:
#80-100, A
#70-79, B
#60-69, C
#50-59, D
#0-49, F
Calificacion = int(input("Ingresa tu calificacion"))
if Calificacion < 49:
     print("Tu nota es F")