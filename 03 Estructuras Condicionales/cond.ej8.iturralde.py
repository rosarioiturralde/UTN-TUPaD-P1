#Escribir un programa que solicite al usuario que ingrese su nombre y el número
# 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción
# seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python 
# para convertir entre mayúsculas y minúsculas.

# Solicitar el nombre al usuario
nombre = input("Ingresa tu nombre: ")

# Mostrar opciones
print("Elige una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")

# Solicitar la opción
opcion = input("Ingresa 1, 2 o 3: ")

# Transformar según la opción
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, ingresa 1, 2 o 3.")