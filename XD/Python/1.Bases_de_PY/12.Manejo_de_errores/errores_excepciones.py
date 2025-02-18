
#el manejo de errores y excepciones en cualquier lenguaje de programacion se refiere a que, cuando un usuario ingresa un dato 
# que no es del tipo de dato esperado en el codigo y el programa lo marca como error, ¿como hacer para que se solventen este
# tipo de errores ?

# edad = int(input('Ingrese su edad: '))

# print('Tu edad es: ', edad * 2)
# aqui se esta pidiendo un tipo de dato entero, pero si el usuario, ya sea por error, digita otro tipo de dato, ¿como se puede arreglar?

#comando Try
# try:
#     edad = int(input('Ingresa tu edad: '))
#     print('Tu edad es: ', edad)
# # cuando el codigo corre bien y el usuario ingresa valores correctos al programa, el codigo correra en esta parte
# except: 
#     print('Ingresaste un valor erroneo')
# # en dado caso de que el usuario digite, en este caso, cualquier cadena de caracteres, en la interfaz del usuario se mostrara 
# # este print

# ahora como hacer para que el programa se repita hasta que el usuario vuelva a ingresar valores ahora corretos sin que el programa se
# cierre
# while True: #repite el ciclo
#     try:
#         edad = int(input('Ingresa tu edad: '))
#         print('Tu edad es: ', edad)
#     # cuando el codigo corre bien y el usuario ingresa valores correctos al programa, el codigo correra en esta parte
#         break #rompe el ciclo en cuanto este apartado se corra 
#     except: 
#         print('Ingresaste un valor erroneo')
#     # en dado caso de que el usuario digite, en este caso, cualquier cadena de caracteres, en la interfaz del usuario se mostrara 
#     # este print

    # comando finally, termina el programa 
# while True: #repite el ciclo
#     try:
#         edad = int(input('Ingresa tu edad: '))
#         print('Tu edad es: ', edad)
#         # cuando el codigo corre bien y el usuario ingresa valores correctos al programa, el codigo correra en esta parte
#         break #rompe el ciclo en cuanto este apartado se corra 
#     except: 
#         print('Ingresaste un valor erroneo')
#         # en dado caso de que el usuario digite, en este caso, cualquier cadena de caracteres, en la interfaz del usuario se mostrara 
#         # este print
#     finally:
#         print('El programa finalizo ')

#excepciones multiples
# while True:
#     try:
#         num1 = int(input('Ingresa un numero: '))
#         res = 100 / num1
#         print(res)
#         break
#     except ZeroDivisionError: 
#         print('No se puede dividir entre cero ')

# while True:
#     try:
#         edad = int(input('ingresa tu edad: '))
#         print('Tu edad es: ', edad)
#         break
#     except ValueError: #si el tipo de dato no es el requerido marca ese error
#         print('Has colocado un valor erroneo')

while True:
    try:
        edad = int(input('ingresa tu edad: '))
        print('Tu edad es: ', edad)
        break
    except KeyboardInterrupt: #si presionas desde el teclado ctrl + c cancelas la ejecucuion 
        print('\nHas cancelado la ejecucion')
        break