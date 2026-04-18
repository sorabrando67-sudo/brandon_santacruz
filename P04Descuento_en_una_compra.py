total = float(input("Ingresa el total de la compra: "))
membresia = input("¿Tienes membresía? (si/no): ")

if total > 1000 and membresia == "si":
    print("Tienes descuento del 20%")
else:
    print("No tienes descuento")