#Escriba un código que califique a los estudiantes según sus puntuaciones:
#80-100, A
#70-79, B
#60-69, C
#50-59, D
#0-49, F
Calificacion = int(input("Ingresa tu calificacion"))
if Calificacion >= 80 and Calificacion <= 100:
    print("Tu nota es A")
elif Calificacion >= 70 and Calificacion <= 79:
    print("Tu nota es B")
elif Calificacion >= 60 and Calificacion <= 69:
    print("Tu nota es C")
elif Calificacion >= 50 and Calificacion <= 59:
    print("Tu nota es D")
else:
    print("Tu nota es F")

#Comprueba si la temporada es otoño, invierno primavera o verano
#septiembre-octubre-noviembre, otoño
#Diciembre-enero-febrero, invierno 
#Marzo-abril-mayo, primavera
#Junio-julio-agosto, Verano
Mes = int(input("Ingrese el mes: "))
