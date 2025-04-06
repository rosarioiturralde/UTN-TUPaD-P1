#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos 
# que se pueden utilizar para predecir la forma de una distribución normal a partir 
# del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y,
# a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, 
# a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la 
# lista numeros_aleatorios, calcule su moda, su mediana y su media y las 
# compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
# Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma: 
# import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 
# elegidos de forma aleatoria.

import random
import statistics

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

# Mostrar los valores calculados
print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar el tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar un sesgo claro con estos valores")