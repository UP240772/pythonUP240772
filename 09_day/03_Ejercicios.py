#Aquí tenemos un diccionario de personas. ¡Modifícalo!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    HabilidadMedia = len(person["skills"])//2
    print(person['skills'][HabilidadMedia])
else:
    print("Error")
#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    TienePython = "Python" in person['skills']
    print(TienePython)
else:
    print("Error")
#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if "skills" in person:
    Habilidades = person['skills']
    if set(Habilidades) == {{'JavaScript', 'React'}}:
        print("El es desarrollador Front-end")
    elif set(Habilidades) >= {'Node', 'Python', 'MongoDB'}:
        print("El es desarrollador back-end")
    elif set(Habilidades) >= {'React', 'Node', 'MongoDB'}:
        print("Es el desarrolador Full-Stack")
    else:
        print("Titulo desconocido")
#* If the person is married and if he lives in Finland, print the information in the following format: 
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")