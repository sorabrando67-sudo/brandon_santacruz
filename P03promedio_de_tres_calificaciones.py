#BRANDON GAEL SANTACRUZ SORIA
# Pedir las tres calificaciones
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# Calcular el promedio
promedio = (cal1 + cal2 + cal3) / 3

# Mostrar el promedio
print("Tu promedio es:", promedio)

# Evaluar si aprueba o reprueba
if promedio >= 6:
    print("Aprobado")
else:
    print("Reprobado")
