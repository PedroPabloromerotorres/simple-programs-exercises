#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

numero = input("Por favor, ingrese un número entero de tres dígitos: ")


if numero.isdigit() and len(numero) == 3:
    
    numero_invertido = numero[::-1]

    print("El número con los dígitos en orden inverso es:", numero_invertido)

else:
    
    print("Error: Debe ingresar un número entero de tres dígitos.")
