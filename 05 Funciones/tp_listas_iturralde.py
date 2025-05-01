#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing 
# con números negativos!
mis_favoritos = ['plantas', 'series', 'comida', 'perros', 'gatos']
print(mis_favoritos[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. 
palabras = []  # Lista vacía

# Agregar tres palabras
palabras.append("perro")
palabras.append("gato")
palabras.append("serie")
print(palabras)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los
# videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", 
# "conejo", "pez"]
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo (índice 1) y el último (índice -1)
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#este programa elimina el valor maximo de la lista.

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar 
# por pantalla los dos primeros.
numeros = list(range(10, 31, 5))  # Del 10 al 30 inclusive, de 5 en 5
print(numeros[:2])  # Mostrar los dos primeros

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en los índices 1 y 2
autos[1] = "amarok"
autos[2] = "hilux"

# Imprimir la lista resultante
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.
dobles = []  # Lista vacía

# Agregar el doble de 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

# Lista inicial
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla. 2
lista_anidada = [
    15,                # lista_anidada[0]
    True,              # lista_anidada[1]
    [25.5, 57.9, 30.6],# lista_anidada[2][0], [2][1], [2][2]
    False              # lista_anidada[3]
]

# Imprimir la lista resultante
print(lista_anidada)
