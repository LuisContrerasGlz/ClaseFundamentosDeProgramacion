"""
Crea un diccionario en Python con la información de un alumno:

nombre

edad

lista de calificaciones

si está aprobado (True/False)

Guarda ese diccionario en un archivo llamado alumno.json usando el módulo json y la función json.dump().

"""

import json

# Diccionario con datos de un alumno
alumno = {
    "nombre": "Juan Pérez",
    "edad": 17,
    "calificaciones": [8, 9, 10, 7],
    "aprobado": True
}

# Guardar en un archivo JSON
with open("alumno.json", "w", encoding="utf-8") as f:
    json.dump(alumno, f, ensure_ascii=False, indent=4)

print("Archivo 'alumno.json' creado correctamente.")