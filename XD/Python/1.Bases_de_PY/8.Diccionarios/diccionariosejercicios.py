'''
En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, 
en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.
'''
'''
{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa","Nicaragua": "Managua", 
"Costa Rica": "San Jose", "Panama": "Panama", 
"Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

diccionario = {"Guatemala": "Ciudad de Guatemala", "Honduras": "Tegucigalpa","Nicaragua": "Managua", 
 "Panama": "Panama", 
"Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('Ingrese un pais para conocer su capital: ')
letra = pais.capitalize() in diccionario #el metodo capitalize convierte la primer letra en mayuscula
#'in' se utiliza para ver que un elemento este dentro de otro 
if letra == True: #condicional para ver que la opcion digitada este en el diccionario
    print('La capital del pais digitado es: ', diccionario[pais.capitalize()])
else: 
    print('El pais no se encuentra en el diccionario')

#para pedir numeros num = int(input('Ingresa el numero: '))



