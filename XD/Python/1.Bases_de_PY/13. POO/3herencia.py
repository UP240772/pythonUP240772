# HERENCIA 
'''
la herencia es la capacidad de crear nuevas clases a partir de clases ya existentes, su principal caracteristica es la reutilizacion del codigo
'''
class Celular(): #clase padre 
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

'''
Las clases hijas heredan metodos y caracteristicas de la clase padre pero la clase padre no tiene los mismos que las clases hijas
'''

class Android(Celular): #clase hija
    def expandir_almacenamiento(self):
        print("Expandiendo almacenamiento")

class Iphone(Celular): #clase hija
    def transferir_archivos(self):
        print("Transfiriendo archivos")

#instancias de los objetos
#-------------------------objeto 1-----------------------------------------------
Celular_Android = Android("Blanco", 64)#instancia de objeto de la clase Android, con los parametros que requiere la clase padre
Celular_Android.expandir_almacenamiento() #metodo propio de la clase

# #metodos heredados de la clase padre
print(Celular_Android.color)
print(Celular_Android.almacenamiento)
Celular_Android.encender()
Celular_Android.apagar()
Celular_Android.info()

#-------------------------objeto 2-----------------------------------------------
Celular_Iphone = Iphone("Negro", 32)#instancia de objeto de la clase Android, con los parametros que requiere la clase padre
Celular_Iphone.transferir_archivos() #metodo propio de la clase

#metodos heredados de la clase padre
print(Celular_Iphone.color)
print(Celular_Iphone.almacenamiento)
Celular_Iphone.encender()
Celular_Iphone.apagar()
Celular_Iphone.info()