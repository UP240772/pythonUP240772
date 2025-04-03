#INICIO DIA 8

#Crea un diccionario vacío llamado perro
PerroVacio = {}

#Añade nombre, color, raza, patas y edad al diccionario de perros.
Perro = {"Nombre":"Kichi", 
   "Edad":"12 años", 
    "Raza":"Pitbull", 
   "Patas":"4"}
print(Perro)

#Cree un diccionario de estudiantes y agregue nombre, apellido, genero, edad, estado civil, habilidades, pais, cuidad y direccion como claves en el diccionario
Estudiantes = {
    "Nombre":"Christian",
    "Apellidos":"Morales Vazquez",
    "Genero":"Hombre",
    "Edad":"18a años",
    "Estado civil":"Soltero",
    "Habilidades":"Bueno en basketball",
    "Pais":"Mexico",
    "Cuidad":"Aguascalienmtes",
    "Direccion":{
        "Calle":"Antonio Hernandez Gallegos",
        "CP":"20206",
    }
}
print(Estudiantes)

#Obtenga la longitud del diccionario del estudiante
print(len(Estudiantes))

#Obtenga el valor de las habilidades y verifique el tipo de dato, debe ser una lista
print(Estudiantes["Habilidades"])

#Modifique los valores de las habilidades agregando una o dos habilidades
Estudiantes["Habilidades"] = "Hiper foco"
print(Estudiantes)

#Obtenga las claves del diccionario como una lista
Claves = Estudiantes.keys()
print(Claves)

#Obtener los valores del diccionario como una lista
Valores = Estudiantes.values()
print(Valores)

#Cambie el diccionario a una lista de tuplas usando el método items()
print(Estudiantes.items())

#Eliminar uno de los elementos del diccionario
Estudiantes.pop("Habilidades")
print(Estudiantes)

#Eliminar uno de los diccionarios
del Perro

print("revisado")