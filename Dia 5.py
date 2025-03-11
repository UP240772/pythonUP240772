#Declarar una lista vacía
ListaVacia = list() 
print(len(ListaVacia)) 

#Declarar una lista con más de 5 elementos
Frutas = ["Manzana", "Naranja", "Mango", "Platano", "Limón"]

#Encuentra la longitud de tu lista
print(len(Frutas))

#Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
PrimerElemento = Frutas[0]
SegundoElemento = Frutas[3]
TercerElemento = Frutas[4]

#Declara una lista llamada mixed_data_types, pon tu(nombre, edad, altura, estado civil, dirección)
MixedDataTypes = ["Christian", "18 Años", "1.72 m", "Soltero", "Laureles del sur"]

#Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Imprima la lista usando print()
print(ItCompanies)

#Imprima el número de empresas en la lista
print(len(ItCompanies))

#Imprima la primera, la segunda y la última empresa.
PrimeroEmp = ItCompanies [0]
SegundaEmp = ItCompanies [2]
TerceraEmp = ItCompanies [6]
print(PrimeroEmp, SegundaEmp, TerceraEmp)

#Imprima el listado después de modificar una de las empresas
ItCompanies [0] = "Meta"
print(ItCompanies)

#Añadir una empresa de TI a it_companies
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
ItCompanies.append("TI")
print(ItCompanies)

#Insertar una empresa de TI en el medio de la lista de empresas
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
ItCompanies.insert(2, "TI")

#Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
print(ItCompanies[0].upper())

#Unir it_companies con una cadena '#; '
Unir = "#; ".join(ItCompanies)
print(Unir)

#Comprueba si una determinada empresa existe en la lista it_companies.
SiExiste =  "Google" in ItCompanies
print(SiExiste)

#Ordenar la lista usando el método sort()
ItCompanies.sort()  
print(ItCompanies)

#Invierta la lista en orden descendente utilizando el método reverse()
ItCompanies.sort(reverse=True)
print(ItCompanies)

#Separa las primeras 3 empresas de la lista.
Facebook_Google_Microsoft = ItCompanies[0:2]
print(Facebook_Google_Microsoft)

#Elimina las últimas 3 empresas de la lista.
ItCompanies.remove("IBM")
ItCompanies.remove("Oracle")
ItCompanies.remove("Amazon")
print(ItCompanies)

#Elimina de la lista las empresas de TI intermedias
ItCompanies.remove("Apple")
print(ItCompanies)

#Eliminar la primera empresa de TI de la lista
ItCompanies.remove("Facebook")
print(ItCompanies)

#Eliminar la o las empresas de TI intermedias de la lista
ItCompanies.remove("Microsoft")
print(ItCompanies)

#Eliminar la última empresa de TI de la lista
print(ItCompanies)

#Eliminar todas las empresas de TI de la lista
del ItCompanies [0:6]

#Destruir la lista de empresas de TI
del ItCompanies

#Únete a las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
FrontEnd_BackEnd = front_end + back_end
print(FrontEnd_BackEnd)

#Después de unir las listas en la pregunta 26. Copie la lista unida y asígnela a una variable full_stack, luego inserte Python y SQL después de Redux.
ItCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
ItCompaniesCopia = ItCompanies.copy()
FullStack = ItCompaniesCopia
FullStack.insert(5, "Python")
print(FullStack)
FullStack.insert(6, "SQL")
print(FullStack)

#Ejercicios: Nivel 2
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Ordena la lista y encuentra la edad mínima y máxima.
edades.sort()
print(edades)

#Agregue la edad mínima y la edad máxima nuevamente a la lista
edades.insert(0, "19")
print(edades)
edades.insert(10, "26")

#Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Media=len(ages)//2
print(Media)
print("Punto 4")
#Find the average age (sum of all items divided by their number )
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Promedio=sum(ages)/len(ages)#La operacion sum() me sirve para sumar toda una cadena o lista sin tener que haser laoperacion de uno por uno 
print(Promedio)
print("Punto 5")
#Find the range of the ages (max minus min)
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
rango=(max-min)
print(rango)
print("Punto 6")
#Compare the value of (min - average) and (max - average), use abs() method
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
diferiencia=abs(max-min)#el metodo abs() se utiliza para medir la distancia de dos puntos .
print(diferiencia)

print("Ejercicio 2")
#Find the middle country(ies) in the countries list
countries_list=['Afghanistan',
 'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
len(countries_list)//2
media=(countries_list[96])
print(media)

print("Ejercicio 3")
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_list=['Afghanistan',
 'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
countries_list.sort()
media=len(countries_list)//2
lista_1=countries_list[:media +1]
lista_2=countries_list[media + 2:]
print(lista_1)
print(lista_2)

print("Ejercicio 4")
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
paises=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
primeros_3=paises[0:3]
ultimos=paises[-4:7]
print("primeros 3: ",primeros_3)
print("Paises escandinabos; ",ultimos)

print("Fin Del Dia 5")


