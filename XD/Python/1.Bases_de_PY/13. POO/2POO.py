#INCLUSION DE PARAMETROS EN LA CLASE 
#se usa para darle mas variedad de caracteristicas de cada objeto

class Celular: 
    # variable_ejemplo = "Ejemplo"
    def __init__(self, color ): #aqui escribimos los parametros iniciales cuando se instancie el objeto
        self.color = color #self es para referenciar que es una variable propia de la clase, el atributo color es propio de este metodo, cada metodo tiene sus propios parametros 
    

    def encender(self, contrasena): #dentro de una clase cada metodo debe tener como parametro self
        print(f"Encendiendo telefono {contrasena}")
        #print(self.color)

    def apagar(self): #dentro de una clase cada metodo debe tener como parametro self
        print("Apagando telefono")


#instancia de la clase para crear objeto
celular1 = Celular("Rojo") #aqui va el argumento color que requiere el metodo constructor
print(celular1.color)
celular1.encender("1234")#llamamos a los metodos con su parametro
celular1.apagar()