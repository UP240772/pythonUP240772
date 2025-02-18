class Celular():
    def __init__(self, color, almacenamiento): 
        self.color = color
        self.almacenamiento = almacenamiento
    def info(self):
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento} Gb")
    def encendido(self,contraseña): 
        print(f'Encendido... {contraseña}')
    def apagar(self):
        print('apagar...')

class Android(Celular):
    def expandir_memoria(self):
        print('Expandiendo memoria...')
class Iphone(Celular):
    def transferir_archivo(self):
        print('Transfiriendo archivos...')

print('Objeto 1 android hijo de celular')
Celular_Android = Android("Negro", "120")

Celular_Android.expandir_memoria()
Celular_Android.apagar()
Celular_Android.info()
print('Objeto 2 Iphone hijo de celular')

iphone = Iphone("Blanco", "64")

iphone.transferir_archivo()
iphone.encendido('face_id')
iphone.info()