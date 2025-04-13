#Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

# Solicitar los dos valores al usuario
inicio = int(input("Ingresa el primer número entero: "))
fin = int(input("Ingresa el segundo número entero: "))

# Asegurarse de que inicio sea menor que fin
if inicio > fin:
    inicio, fin = fin, inicio

# Sumar los números entre los dos valores (excluyéndolos)
suma = 0
for i in range(inicio + 1, fin):
    suma += i

# Mostrar el resultado
print(f"La suma de los números entre {inicio} y {fin} es: {suma}")

##tiene error cuando los numeros son iguales o no hay numeros en el medio ya que la suma de cero, corregir eso
