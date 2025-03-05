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
TercerElemento = Frutas[5]

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
TerceraEmp = ItCompanies [7]
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

