#Obtener la información del usuario mediante input(“Ingrese su edad:”). Si el usuario tiene 18 años o más, indique: Tiene edad suficiente para conducir. Si es menor de 18 años, indique que espere los años que faltan. Resultado:
Edad = float(input("Ingrese su edad: "))
if Edad < 18:
    print("No tienes edad suficiente para aprender a conducir")
else:
    print("Tienes la edad suficiente para aprender a conducir")