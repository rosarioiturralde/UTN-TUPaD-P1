#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# 4dígitos que contiene.

# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Convertir a valor absoluto para contar dígitos sin considerar el signo
numero_absoluto = abs(numero)

# Contar los dígitos convirtiendo el número a cadena
cantidad_digitos = len(str(numero_absoluto))

# Mostrar el resultado
print(f"El número tiene {cantidad_digitos} dígito(s).")