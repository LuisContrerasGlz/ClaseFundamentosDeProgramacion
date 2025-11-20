"""
Lee alumnos.csv y conviértelo en una lista de diccionarios.
Cada diccionario debe tener las claves: nombre, edad, grupo.
Después, imprime solo los nombres de los alumnos.

"""

import csv

lista_alumnos = []

with open("alumnos.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Usa la primera fila como encabezados
    for fila in reader:
        lista_alumnos.append(dict(fila))

print("Lista de diccionarios:")
print(lista_alumnos)

print("\nNombres de los alumnos:")
for alumno in lista_alumnos:
    print(alumno["nombre"])

