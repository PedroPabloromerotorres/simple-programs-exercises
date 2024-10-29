#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
# Donde NC es el promedio de certámenes, 
 # NL el promedio de laboratorio y 
 # NF la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3


Certamen1 = float(input("Ingrese la nota del primer certamen: "))
Certamen2 = float(input("Ingrese la nota del segundo certamen: "))
NL = float(input("Ingrese la nota de laboratorio: "))


NF_necesaria = 60


Certamen3 = (NF_necesaria - (NL * 0.3)) * (3 / 0.7) - Certamen1 - Certamen2

if Certamen3 >= 0:
    print(f"La nota que necesita en el tercer certamen 3 para aprobar es: {Certamen3:.2f}")
else:
    print("Ya ha aprobado el ramo, no necesita ninguna nota en el tercer certamen.")
