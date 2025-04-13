#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, elm
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1  # valor inicial que no coincida

print("¡Adivina el número entre 0 y 9!")

while adivinanza != numero_secreto:
    adivinanza = int(input("Tu intento: "))
    intentos += 1

print(f"¡Correcto! El número era {numero_secreto}.")
print(f"Lo lograste en {intentos} intento(s).")
