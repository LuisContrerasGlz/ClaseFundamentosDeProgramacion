"""
Usando el archivo alumno.json, léelo con json.load() y muestra:

Nombre del alumno

Edad

Lista de calificaciones

Promedio de calificaciones

Si está aprobado o no
"""

import json

# Leer el archivo JSON
with open("alumno.json", "r", encoding="utf-8") as f:
    alumno = json.load(f)

# Calcular promedio
calificaciones = alumno["calificaciones"]
promedio = sum(calificaciones) / len(calificaciones)

# Mostrar información
print("Nombre:", alumno["nombre"])
print("Edad:", alumno["edad"])
print("Calificaciones:", calificaciones)
print("Promedio:", promedio)
print("Aprobado:", alumno["aprobado"])

