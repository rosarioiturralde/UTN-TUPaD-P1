#Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.


total = 0
numero = int(input("Ingresa un número entero (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingresa un número entero (0 para terminar): "))

print(f"La suma total de los números ingresados es: {total}")
