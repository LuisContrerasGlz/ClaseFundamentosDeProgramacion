"""
Crea un archivo llamado alumnos.csv con las columnas:

nombre

edad

grupo

Agrega al menos 5 alumnos usando csv.writer().

"""

import csv

# Datos de ejemplo
alumnos = [
    ["nombre", "edad", "grupo"],      # encabezados
    ["Luis", 18, "4A"],
    ["Ana", 17, "4B"],
    ["María", 18, "4A"],
    ["Carlos", 17, "4C"],
    ["Sofía", 19, "4B"]
]

# Crear archivo CSV
with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(alumnos)

print("Archivo 'alumnos.csv' creado correctamente.")
