#METODO CONSTRUCTOR
    
'''
a veces se necesita crear objetos con instancias en un estado inicial, las clases tienen un metodo especial que se denomina init o metodo constructor
'''

class Celular: 
    def __init__(self, marca, compañia): #aqui escribimos los parametros iniciales cuando se instancie el objeto
        self.color = "Rojo" #self es para referenciar que es una variable propia d la clase
        self.tamaño = "10"

    def encender(self): #dentro de una clase cada metodo debe tener como parametro self
        print("Encendiendo telefono")

    def apagar(self): #dentro de una clase cada metodo debe tener como parametro self
        print("Apagando telefono")

#instancia de la clase para crear objeto
celular1 = Celular()
#celular2 = Celular()

print(celular1.color)#imprimimos las instancias del metodo constructor 

celular1.encender()#llamamos a los metodos 



