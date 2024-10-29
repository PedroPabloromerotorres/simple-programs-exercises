#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75

primeranota = float(input("Primera nota: "))
segundanota = float(input("Segunda nota: "))
tercenota = float(input("Tercera nota: "))
cuartanota = float(input("Cuarta nota: "))

promedio = (primeranota + segundanota + tercenota + cuartanota) / 4

print("El promedio es: ", promedio)