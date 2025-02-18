'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres ultimas letras, 
tiene que decir que riman, si coinciden solo las dos ultimas letras, tiene que decir que riman un poco, 
si solo coincide una o ninguna, que no riman  
'''

palabra1 = input("Ingresa la primer palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3: 
    print("No rima porque tiene menos de 3 caracteres ")
elif palabra1[-3 : ] == palabra2[-3 : ]: 
    print("Las palabras riman")
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Las palabras riman un poco ")
else: 
    print("Las palabras no riman ")
    