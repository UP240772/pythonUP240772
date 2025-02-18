nombre = input("ingresa tu nombre ")
edad = int(input("Ingresa tu edad "))

if nombre.capitalize() == 'Juan':
    if edad >= 18: 
        print('Tu eres Juan y tienes mayoria de edad')
    else:
        print('Eres Juan pero no eres mayor de edad')
else:
    print('Tu no eres Juan')