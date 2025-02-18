from abc import ABC, abstractmethod #libreria para crear clases abstractas

#ABSTRACCION 
'''
la abstraccion es un modelo de un objeto o fenomeno en el mundo real, confinado a un contexto particular, y representa con mucha presicion todos los datos relacionados con ese contexto, ignorando el resto 
'''

# para usar la abstraccion debemos hacer de nuestra clase una clase abstracta para asi esta ya no pueda ser instanciada modulo abc

class Celular(ABC): #se hace uso de ABC como parametro para hacer abstracta la clase 
    @abstractmethod #con esto nuestra clase ya no puede ser instanciada, solo las clases que heredan de esta pueden instanciarse 
    def __init__(self, color, almacenamiento): 
        self.color = color
        self.almacenamiento = almacenamiento

    def info(self): 
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento} GB")

    def encender(self):
        print("Encendiendo celular")

    def apagar(self):
        print("Apagar")


class Android(Celular): #clase hija
    def __init__(self, color, almacenamiento): #para poder instanciar clases hijas todas laclases deben tener esto: constructor y super
        super(Android, self).__init__(color, almacenamiento) #funcion super, permite conservar metodos o atributos de la clase padre, necesita argumentos

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento")

class Iphone(Celular): #clase hija
    def transferir_archivos(self):
        print("Transfiriendo archivos")


celular_Android = Android("rojo", 128)
celular_Android.expandir_almacenamiento()

