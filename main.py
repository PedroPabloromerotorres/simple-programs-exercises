#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo,
# y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267

import math

a = float(input("Ingrese la longitud del cateto a: "))

b = float(input("Ingrese la longitud del cateto b: "))

c = math.sqrt(a**2 + b**2)

print(f"La longitud de la hipotenusa c es: {c:.2f}")
