# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿En qué mes estás? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Calcular una fecha numérica para facilitar comparaciones
# Por ejemplo, 21 de marzo será 321 (mes 3, día 21)
fecha = mes * 100 + dia

# Determinar estación según el hemisferio
if hemisferio == "N":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no válido"

# Mostrar el resultado
print("Estás en:", estacion)