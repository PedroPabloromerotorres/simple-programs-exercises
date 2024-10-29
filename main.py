#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6

hora_actual = int(input("Ingrese la hora actual (0-23): "))

horas_a_sumar = int(input("Ingrese la cantidad de horas a sumar: "))

nueva_hora = (hora_actual + horas_a_sumar) % 24

print(f"En {horas_a_sumar} horas, el reloj marcará las {nueva_hora}.")