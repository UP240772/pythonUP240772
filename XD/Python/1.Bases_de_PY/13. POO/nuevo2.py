class Personajes:
    def __init__(self, color, nombre, letra, ruca): 
        self.ropa = 'Plomero'
        self.guantes = 'Blanco'
        self.bigote = 'bigote'
        self.color = color
        self.nombre = nombre
        self.letra = letra
        self.ruca = ruca

    def saltar(self):
        print('salto')

    def correr(self):
        print('corre')

    def tomar_objetos(self, objeto):
        print('tomo el objeto', objeto)

class Personajes_antagonicos(Personajes):
    def Ser_malos_muy_malos(self):
        print('soy malo')
        print('aayy..el diablo')
    

class Personajes_principales(Personajes):
    def Ser_buenos(self):
        print('soy mas bueno que el pan')


# aqui acabamos de crear una instancia de nuestra clase hija Personajes_antagonicos
wario = Personajes_antagonicos('amarillo', 'Wario', 'W', 'No tiene')


# se puede acceder a los metodos de la classe hija

wario.Ser_malos_muy_malos()

# ademas podemos acceder a los metodos de la clase padre

print(wario.ruca)

