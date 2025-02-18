#metodo format
nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

print(nombre)
print(edad)

# concatenacion
print(nombre, edad) 
print('hola ', nombre, ' tienes ', edad, ' años')

# format
print('hola {} tienes {} años'.format(nombre, edad)) #reemplaza las variables en los corchetes en el orden ingresado 
