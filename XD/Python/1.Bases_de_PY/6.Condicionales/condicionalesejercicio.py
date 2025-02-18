# Ejercicio 1
# Crear un programa que le pida al usuario que ingrese una letra, si esta es vocal debera mostrar un mensaje 'es vocal'
# de lo contrario debera mostrar 'no es vocal'

letra = input("Ingresa una letra: ")
# if letra.lower() == "a":
#     print("Es una vocal")
# else:
#     if letra.lower() == "e":
        # print("Es una vocal")
#     else: 
#         if letra.lower() == "i":
            # print("Es una vocal")
#         else:
#             if letra.lower() == "o":
#                 print("Es una vocal")
#             else:
#                 if letra.lower() == "u":
#                     print("Es una vocal")
#                 else:
#                     print("No es una vocal")

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")
























