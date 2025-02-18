# Escribir un programa que dado un numero entero muestre su valor absoluto.
# NOTA: para los numeros positivos su valor absoluto es igual al mismo numero, mientras que para los numeros negativos, 
# su valor absoluto es el numero multiplicado por -1.   

numero = int(input("Ingresa el numero sin decimal: "))
# if numero > 0:
#     print("El valor absoluto de {} es: {} ".format(numero, numero))
# else: 
#     print("El valor absoluto de {} es: ".format(numero), numero * -1)
print(abs(5)) #metodo para calcular el valor absoluto
print(abs(numero))
print("El valor absoluto de {} es: ".format(numero), abs(numero))
