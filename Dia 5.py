#Declarar una lista vacía
ListaVacia = list() 
print(len(ListaVacia)) 

#Declarar una lista con más de 5 elementos
Frutas = ["Manzana", "Naranja", "Mango", "Platano", "Limón"]

#Encuentra la longitud de tu lista
print(len(Frutas))

#Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
PrimerElemento = Frutas[0]
SegundoElemento = Frutas[3]
TercerElemento = Frutas[4]

#Declara una lista llamada mixed_data_types, pon tu(nombre, edad, altura, estado civil, dirección)
MixedDataTypes = ["Christian", "18 Años", "1.72 m", "Soltero", "Laureles del sur"]

#Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Imprima la lista usando print()
print(ItCompanies)

#Imprima el número de empresas en la lista
print(len(ItCompanies))

#Imprima la primera, la segunda y la última empresa.
PrimeroEmp = ItCompanies [0]
SegundaEmp = ItCompanies [2]
TerceraEmp = ItCompanies [6]
print(PrimeroEmp, SegundaEmp, TerceraEmp)

#Imprima el listado después de modificar una de las empresas
ItCompanies [0] = "Meta"
print(ItCompanies)

#Añadir una empresa de TI a it_companies
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
ItCompanies.append("TI")
print(ItCompanies)

#Insertar una empresa de TI en el medio de la lista de empresas
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
ItCompanies.insert(2, "TI")

#Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
print(ItCompanies[0].upper())

#Unir it_companies con una cadena '#; '
Unir = "#; ".join(ItCompanies)
print(Unir)

#Comprueba si una determinada empresa existe en la lista it_companies.
SiExiste =  "Google" in ItCompanies
print(SiExiste)

#Ordenar la lista usando el método sort()
ItCompanies.sort()  
print(ItCompanies)

#Invierta la lista en orden descendente utilizando el método reverse()
ItCompanies.sort(reverse=True)
print(ItCompanies)

#Separa las primeras 3 empresas de la lista.
Facebook_Google_Microsoft = ItCompanies[0:2]
print(Facebook_Google_Microsoft)

#Elimina las últimas 3 empresas de la lista.
ItCompanies.remove("IBM")
ItCompanies.remove("Oracle")
ItCompanies.remove("Amazon")
print(ItCompanies)

#Elimina de la lista las empresas de TI intermedias
ItCompanies.remove("Apple")
print(ItCompanies)

#Eliminar la primera empresa de TI de la lista
ItCompanies.remove("Facebook")
print(ItCompanies)

#Eliminar la o las empresas de TI intermedias de la lista
ItCompanies.remove("Apple", "Microsoft")
print(ItCompanies)

#Eliminar la última empresa de TI de la lista
ItCompanies.remove("Amazon")
print(ItCompanies)

#Eliminar todas las empresas de TI de la lista
del ItCompanies [0:6]

#Destruir la lista de empresas de TI
del ItCompanies

#Únete a las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
FrontEnd_BackEnd = front_end + back_end
print(FrontEnd_BackEnd)

#Después de unir las listas en la pregunta 26. Copie la lista unida y asígnela a una variable full_stack, luego inserte Python y SQL después de Redux.
ItCompaniesCopia = ItCompanies.copy()
FullStack = ItCompaniesCopia
FullStack.insert(5, "Python")
print(FullStack)
FullStack.insert(6, "SQL")
print(FullStack)

#Ejercicios: Nivel 2
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordena la lista y encuentra la edad mínima y máxima.
edades.sort()
print(edades)

#Agregue la edad mínima y la edad máxima nuevamente a la lista
edades.insert(0, "19")
print(edades)
edades.insert(10, "26")

#Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)
Print(len(edades))
