from abc import ABC, abstractmethod #libreria para crear clases abstractas

#POLIMORFISMO
'''
es la capacidad de un programa para detectar la clase real de un objeto y llamar a su implementacion, es decir, todas las subclases que heredan de una clase padre tienen diferencias en sus metodos, estan sobre escritos 
'''

class Celular(ABC): #se hace uso de ABC como parametro para hacer abstracta la clase 
    @abstractmethod #con esto nuestra clase ya no puede ser instanciada, solo las clases que heredan de esta pueden instanciarse 
    def __init__(self, color, almacenamiento): 
        self.color = color
        self.almacenamiento = almacenamiento

    def info(self): 
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento} GB")

    @abstractmethod 
    def encender(self):
        print("Encendiendo clase padre")

    def apagar(self):
        print("Apagar")


class Android(Celular): #clase hija
    def __init__(self, color, almacenamiento): #para poder instanciar clases hijas todas laclases deben tener esto: constructor y super
        super(Android, self).__init__(color, almacenamiento) #funcion super, permite conservar metodos o atributos de la clase padre, necesita argumentos

    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento")

    #sobre escritura del metodo
    def encender(self): 
        print("Android encendido")
        super(Android, self).encender() #para llamar al metodo de la clase padre usamos el comando super 

class Iphone(Celular): #clase hija
    def __init__(self, color, almacenamiento): #para poder instanciar clases hijas todas laclases deben tener esto: constructor y super
        super(Iphone, self).__init__(color, almacenamiento) #funcion super, permite conservar metodos o atributos de la clase padre, necesita argumentos
        
    def transferir_archivos(self):
        print("Transfiriendo archivos")

    #sobreescribir codigo
    def encender(self): 
        print("Iphone encendido")
        super(Iphone, self).encender()

celular_Android = Android("rojo", 128)
celular_Android.encender()

celular_Iphone = Iphone("Blanco", 64)
celular_Iphone.encender()