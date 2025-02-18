
# Variables in Python

first_name = 'Christian'
last_name = 'Vazquez'
country = 'Mexico'
city = 'Aguascalientes'
age = 18
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Christian', 
    'lastname':'Vazuez', 
    'country':'Mexico',
    'city':'Aguascalientes'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Christian', 'Vazquez', 'Aguascalientes', 18, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

##Area de un circulo
radio = int(input ("Ingresa el radio del circulo"))
pi = 3.14159
areaOfCircle = 2 * pi ** 2
circumOfCircle = 2 * pi * radio 
print('The area of circle is ', areaOfCircle)
print('The circumference of the circle is ', circumOfCircle)

##Datos personales
nombre = str(input("Ingrese sus nombres: "))
apellido = str(input("Ingrese sus apellidos: "))
Residencia = str(input("Ingrese su direccion: "))
Edad = str(input("Ingrese su edad: "))

print("Tu nombre es: " + nombre)
print("Tu apellido es: " + apellido)
print("Tu vives en: " + Residencia)
print("Tu edad es: " + Edad)