#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Solicitar al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if numero >= 0:
    suma = sum(range(numero + 1))  # Suma de los números de 0 hasta el número ingresado
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")
