'''
un condicional es una funcion de codigo propia de los lenguajes de programacion la cual nos permite validar acciones o, como su nombre lo dice, condicionar una serie de acciones a un comando, comparacion, cambio en una variable, etc 
'''

#para comprender un poco mejor los condicionales veamos el siguiente ejemplo

#programa que diga si eres mayor de edad 

# edad = 15

# if edad >= 18:
#     print('Eres mayor de edad, puedes obtener tu INE ')
# else:
#     print('No eres mayor de edad, no puedes obtener INE ')

# Para py se necesita cuidar mucho la identacion

#elif

letra = 'E'

if letra.lower() == 'a':
    print('Esta vocal es la letra "A"')
elif letra.lower() == 'e':
    print('Esta vocal es la letra "E"')
elif letra.lower() == 'i':
    print('Esta vocal es la letra "I"')
elif letra.lower() == 'o':
    print('Esta vocal es la letra "O"')
else: 
    print('Esta vocal es la letra "U"')



