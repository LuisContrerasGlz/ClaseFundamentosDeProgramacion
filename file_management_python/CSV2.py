"""
Lee el archivo alumnos.csv y muestra cada fila con el formato:

Nombre: ____, Edad: ____, Grupo: ____

Usa csv.reader().

"""

import csv

with open("alumnos.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # Saltar encabezado
    encabezado = next(reader)

    for fila in reader:
        nombre, edad, grupo = fila
        print(f"Nombre: {nombre}, Edad: {edad}, Grupo: {grupo}")
