#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)