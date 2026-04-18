edad = int(input("Ingresa tu edad: "))
tiene_credencial = input("¿Tienes credencial? (si/no): ")
llueve = input("¿Está lloviendo? (si/no): ")

# Uso de AND
if edad >= 18 and tiene_credencial == "si":
    print("Puedes entrar (cumples con ambos requisitos)")
else:
    print("No puedes entrar")

# Uso de OR
if edad >= 18 or tiene_credencial == "si":
    print("Cumples al menos un requisito")
else:
    print("No cumples ningún requisito")

# Uso de NOT
if not (llueve == "si"):
    print("Puedes salir, no está lloviendo")
else:
    print("Quédate en casa, está lloviendo")