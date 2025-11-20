"""
Crea una lista con al menos 3 alumnos, donde cada alumno tenga:

nombre

grupo

lista de materias

diccionario de calificaciones por materia

Guarda la lista en un archivo llamado grupo.json.

"""

import json

grupo = [
    {
        "nombre": "Ana",
        "grupo": "4A",
        "materias": ["Mate", "Prog", "BD"],
        "calificaciones": {"Mate": 9, "Prog": 10, "BD": 8}
    },
    {
        "nombre": "Luis",
        "grupo": "4B",
        "materias": ["Mate", "Prog"],
        "calificaciones": {"Mate": 7, "Prog": 9}
    },
    {
        "nombre": "María",
        "grupo": "4A",
        "materias": ["BD", "Redes"],
        "calificaciones": {"BD": 10, "Redes": 9}
    }
]

with open("grupo.json", "w", encoding="utf-8") as f:
    json.dump(grupo, f, ensure_ascii=False, indent=4)

print("Archivo 'grupo.json' creado correctamente.")

