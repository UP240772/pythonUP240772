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
Frase = "Codificacion para todos"
