# Escribir una tupla con los meses del año, 
# luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 
'diciembre')

mes = int(input('Ingrese el numero del mes que desea consultar: '))
print('El mes correspondiente a la opcion digitada es: ', tupla[mes])
