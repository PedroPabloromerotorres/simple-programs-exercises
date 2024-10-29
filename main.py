#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19

numero = float(input("Ingrese un número real: "))

parte_decimal = numero - int(numero)

if parte_decimal != 0:

    print(f"La parte decimal de {numero} es: {parte_decimal}")

else:
    print(f"{numero} no tiene parte decimal.")
