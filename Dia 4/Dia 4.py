#Concatenar palabras
Primera_palabra  = "Treinta"
Segunda_palabra = "dias"
Tercera_palabra = "de"
Cuarta_palabra = "Python"
Espacio = " "
FraseCompleta = Primera_palabra + Espacio + Segunda_palabra + Espacio + Tercera_palabra + Espacio + Cuarta_palabra
print (FraseCompleta)

#Concatenar una cadena 
PrimeraPalabra = "Codificacion"
SegundaPalabra = "para"
TerceraPalabra = "todos"
Frase = PrimeraPalabra + Espacio + SegundaPalabra + Espacio + TerceraPalabra
print(Frase)

#Declare una variable llamada empresa y asígnele un valor inicial "Codificación para todos".
Empresa = Frase

#Imprima la variable empresa utilizando print() .
print (Empresa)

#Imprima la longitud de la cadena de la empresa utilizando el método len() y print() .
print(len(Empresa))

#Cambie todos los caracteres a letras mayúsculas utilizando el método upper() .
print(Empresa.upper())

#Cambie todos los caracteres a letras minúsculas utilizando el método lower() .
print(Empresa.lower())

#Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All .
print(Frase.capitalize())
print(Frase.title())
print(Frase.swapcase())

#Recortar (cortar) la primera palabra de la cadena Codificación para todos .
Destajada = Empresa[12:]
print(Destajada)

#Compruebe si la cadena Codificación Para Todos contiene una palabra Codificación utilizando el método index, find u otros métodos.
Subcadena = Frase
print(Subcadena.find("Codificacion")) #1

#Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.
print(Empresa.replace("Codificacion", "Python"))

#Cambie Python para todos a Python para todos utilizando el método de reemplazo u otros métodos.
print(Empresa.replace("Codificacion para todos", "Python para todos"))

#Divida la cadena 'Coding For All' usando el espacio como separador (split()).
Cadena = Frase
print(Cadena.split())
Cadena = "Codificacion, para, todos"
print(Cadena.split(" , "))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma.
A1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(A1.split())
A1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(A1.split(" , "))

#¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos ?
Frase = "Codificacion para todos"
print(Frase[0])

#¿Cuál es el último índice de la cadena Codificación Para Todos .
Frase = "Codificacion para todos"
print(Frase[22])

#¿Qué carácter está en el índice 10 en la cadena "Codificación para todos"?
Frase = "Codificacion para todos"
print(Frase[10])

#Crea un acrónimo o una abreviatura para el nombre 'Python para todos'
Acronimo = "PPT"

#Crea un acrónimo o una abreviatura para el nombre 'Coding For All'.
Acronimo = "CFA"

#Utilice el índice para determinar la posición de la primera aparición de C en Codificación para todos.
Frase = "Codificacion para todos"
print(Frase.find("C"))

#Utilice el índice para determinar la posición de la primera aparición de F en Codificación para todos.
Frase = "Codificacion para todos"
print(Frase.find("f"))

#Utilice rfind para determinar la posición de la última aparición de l en Coding For All People.
Frase = "Codificacion para todos"
print(Frase.rfind("i"))

#Utilice index o find para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración
#'No puedes terminar una oración con porque porque porque es una conjunción'
Frase = "No puedes terminar una oración con porque porque porque es una conjunción"
print(Frase.find("porque"))

#Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración
#'No puedes terminar una oración con porque porque porque es una conjunción'
Frase = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(Frase.rfind("porque"))

#Elimina la frase 'porque porque porque' en la siguiente oración:
#'No puedes terminar una oración con porque porque porque es una conjunción'
Frase =  'No puedes terminar una oración con porque porque porque es una conjunción'
print("Frase")
primer_porque = Frase [0:31]
print(primer_porque)
ultimo_porque = Frase [54:]
print(ultimo_porque) 

#Encuentra la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 
#'No puedes terminar una oración con porque porque porque es una conjunción'
Frase = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(Frase.find("porque"))

#Elimina la frase 'porque porque porque' en la siguiente oración:
#'No puedes terminar una oración con porque porque porque es una conjunción'
Frase = 'No puedes terminar una oración con porque porque porque es una conjunción'
print("Frase")
primer_porque = Frase [0:31]
print(primer_porque)
ultimo_porque = Frase [54:]
print(ultimo_porque)

#¿''Coding For All' comienza con una subcadena Coding ?
Frase = "Codificacion para todos"
print(Frase.startswith("Codificacion"))

#¿'Coding For All' termina con una subcadena 'coding '?
Frase = "Codificacion para todos"
print(Frase.endswith("Codificacion"))

#'Codificación para todos', elimina los espacios finales izquierdo y derecho en la cadena dada.
Frase = "      Codificacion para todos      "
print(Frase.strip("       "))

#¿Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier()?
#30 días de Python
#Treinta días de Python
Frase = "30 dias de Python"
print(Frase.isidentifier())
Frase = "Treinta dias de Python"
print(Frase.isidentifier())

#La siguiente lista contiene los nombres de algunas bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacios.
lib =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
Resultado = " # ".join(lib)
print(Resultado)

#Utilice la secuencia de escape de nueva línea para separar las siguientes oraciones.
#I am enjoying this challenge.
#I just wonder what is next.
print("I\nam\nenjoying\nthis\nchallenge.")
print("I\njust\nwonder\nwhat\nis\nnext.")

#Utilice una secuencia de escape de tabulación para escribir las siguientes líneas.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#Utilice el método de formato de cadena para mostrar lo siguiente:
radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

#Realice lo siguiente utilizando métodos de formato de cadena:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a = 8
b = 6
suma = a + b
resta = a - b
Multiplicacion = a * b
Division = a / b
Porcentaje = a % b
Potencia = a ** b
Divf = a // b


