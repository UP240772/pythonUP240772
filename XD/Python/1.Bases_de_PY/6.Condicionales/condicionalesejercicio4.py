'''
Crear un programa que le permita al usuario elegir un candidato por el cual votar.
las posibilidades son: 
candidato A, por el partido rojo 
candidato B, por el partido verde
candidato C, por el partido azul
segun el candidato elegido, de debe imprimir el mensaje "usted ha votado por el partido [color del partido elegido]"
si el usuario no ingresa una opcion que corresponde a ninguno de los candidatos disponibles, indicara "opcion erronea" 
'''

opcion = input("Ingresa la opcion de tu candidato ")
if opcion.upper() == "A":
    print("Usted escogio el candidato rojo")
elif opcion.upper() == "B":
    print("Usted escogio el cadidato verde")
elif opcion.upper() == "C": 
    print("Usted escogio el candidato azul")
else: 
    print("Opcion invalida")

