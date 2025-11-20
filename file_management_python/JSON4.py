"""
Abre grupo.json, pide al usuario el nombre de un alumno y, si lo encuentra, muestra:

Sus materias

Sus calificaciones

Su promedio

Si no existe, muestra un mensaje indicando que no se encontró.
"""

import json

# Leer el archivo grupo.json
with open("grupo.json", "r", encoding="utf-8") as f:
    grupo = json.load(f)

nombre_buscar = input("Ingresa el nombre del alumno que deseas buscar: ")

encontrado = False

for alumno in grupo:
    if alumno["nombre"].lower() == nombre_buscar.lower():
        encontrado = True
        print("\nAlumno encontrado:")
        print("Nombre:", alumno["nombre"])
        print("Grupo:", alumno["grupo"])
        print("Materias:", alumno["materias"])
        print("Calificaciones:", alumno["calificaciones"])

        # Calcular promedio a partir del diccionario de calificaciones
        califs = alumno["calificaciones"].values()
        promedio = sum(califs) / len(califs)
        print("Promedio:", promedio)
        break

if not encontrado:
    print("Alumno no encontrado en el archivo.")
