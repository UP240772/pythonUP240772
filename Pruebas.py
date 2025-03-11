print("Nivel 1")
print("Ejercicio 1")
#Declare an empty list
lista=list()#En este ejercicio cee una lista paro la deje bacia
print(lista)

print("Ejercicio 2")
#Declare a list with more than 5 items
lista_de_bebidas=["agua","soda","jugo","sidral","tequila"]
print(lista_de_bebidas)

print("Ejercicio 3")
#Find the length of your list
lista=["auto","Camion","motosiceta"]
longitud=len(lista)#En esta operacion verifique la longitud de mi lista con el metodo len()
print(longitud)

print("Ejercicio 4")
#Get the first item, the middle item and the last item of the list
lista=["1","2","3","4","5"]
longitud=len(lista)
primer_elemento=lista[0]#En este ejarcicio determine los elementos de la lista como la inicial la media y el elemento final
elemento_medio=longitud//2
ultimo_elemento=lista[-1]
print(primer_elemento)
print(elemento_medio)
print(ultimo_elemento)

print("Ejercicio 5")
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Cesar","18","1.74","soltero","Calle celso rodriguez #13 Rancho San Martin"]
print(mixed_data_types)#Aqui solo declare la bariable con el nombre de la lista.

print("Ejercicio 6")
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print(it_companies)

print("Ejercicio 7")
#Print the list using print()
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print(it_companies)

print("Ejercicio 8")
#Print the number of companies in the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
longitud=len(it_companies)
print(it_companies[0])
print(it_companies[1])
print(it_companies[2])#Solo medi la longitud de la lista y a cada balor le asigne un numero y lo imprimi.
print(it_companies[3])
print(it_companies[4])
print(it_companies[5])
print(it_companies[6])

print("Ejercicio 9")
#Print the first, middle and last company
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
longitud=len(it_companies)
print(it_companies[0])
print(it_companies[-1])#Imprimi el primer y ultimo valor de las compañias.

print("Ejercicio 10")
#Print the list after modifying one of the companies
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print(it_companies)
Lista_Modificada=it_companies[0]="Python"#Aqui solo denomine uno de los valores de la lista con otro valor.
print("\n Lista Modificada")
print(it_companies)

print("Ejercicio 11")
#Add an IT company to it_companies
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print("\n Lista sin agregar nada",it_companies)
Add=it_companies.append("IT")#el metodo .append()se utiliza para agregar algo a la lista .
print("\n Lista con IT company agragada")
print(it_companies)

print("Ejercicio 12")
#Insert an IT company in the middle of the companies list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print("Sin agregar IT")
print(it_companies)
medio=len(it_companies)//2
add="IT"
Agregado_medio=it_companies.insert(medio,add)#El metodo .insert()nos sirve para incertar datos a la lista con la opcion de ubicarla donde queramos.
print("Con IT agregado medio")
print(it_companies)

print("Ejercicio 13")
#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print("Sin eliminar")
print(it_companies)
eliminacion=it_companies.remove("IBM")#el metodo remove nos sirve para eliminar el primer dato en una lista o cadena dependirndo de lo que le pida que elimine
print("Ya eliminado IBM")
print(it_companies)

print("Ejercicio 14")
#Join the it_companies with a string '#;  '
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
print("sin unir")
print(it_companies)
concatenacion="#;  ".join(it_companies)# El metodo .join() se utiliza para la concatenacion o union de una lista o cadena
print("ya concatenado")
print(concatenacion)

print("Ejercicio 15")
#Check if a certain company exists in the it_companies list.
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
compañia_buscada="Google" 
if compañia_buscada in it_companies:#en esteejercicio solo declare el dato buscado y utilize el if y el else para decir si si esta o no
   print(f"{compañia_buscada} si esta en la lista")
else: print(f"{compañia_buscada} no esta en la lista")

print("Ejercicio 16")
#Sort the list using sort() method
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)#La funcion sort() se utiliza para ordenar enumeros en orden acendete o decendente o listas y cadenas de manera alfabetica.

print("Ejercicio 17")
#Reverse the list in descending order using reverse() method
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
it_companies.reverse()#El metodo .reverce() se utiliza para boltear una lista o cadena osea lo que estaa el final ahora estara al inicio.
print(it_companies)

print("Ejercicio 18")
#Slice out the first 3 companies from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"][0:3]# aqui pedi que solo me mostrara cierto nomero de texto
print(it_companies)

print("Ejercicio 19")
#Slice out the last 3 companies from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"][4:7]
print(it_companies)

print("Ejercicio 20")
#Slice out the middle IT company or companies from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
medio=len(it_companies)//2
print(it_companies[3])

print("Ejercicio 21")
#Remove the first IT company from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
IT_company=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
it_companies.remove(IT_company[0])
print(it_companies)

print("Ejercicio 22")
#Remove the middle IT company or companies from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
IT_company=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
long=len(IT_company)//2
it_companies.remove(IT_company[long])
print(it_companies)

print("Ejercicio 23")
#Remove the last IT company from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
IT_company=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
it_companies.remove(IT_company[-1])
print(it_companies)

print("Ejercicio 24")
#Remove all IT companies from the list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
IT_company=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
All=it_companies.remove(IT_company[6])
print(All)

print("Ejercicio 25")
#Destroy the IT companies list
it_companies=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
IT_company=["Facebook", "Google","Microsoft","Apple","IBM", "Oracle", "Amazon"]
IT_company.clear()# El metodo clear() se utiliza para destruir aldo o eliminar algo dentro de una cadena o lista.
print(IT_company)

print("Ejercicio 26")
#Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print("".join(front_end))
print("".join(back_end))

print("Ejercicio 26")
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=["Python","SQL"]
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(" ".join(front_end))
print(" ".join(back_end))
print(" ".join(full_stack))

print("Nivel 2")

print("Ejercicio 1")
#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
#Add the min age and the max age again to the list
#Find the median age (one middle item or two middle items divided by two)
#Find the average age (sum of all items divided by their number )
#Find the range of the ages (max minus min)
#Compare the value of (min - average) and (max - average), use abs() method
print("Punto 1")
#Sort the list and find the min and max age
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort(reverse=True)
print(ages)
print("Punto 2")
#Add the min age and the max age again to the list
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
max=max(ages)
min=min(ages)
print(min)
print(max)
print("Punto 3")
#Find the median age (one middle item or two middle items divided by two)
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

