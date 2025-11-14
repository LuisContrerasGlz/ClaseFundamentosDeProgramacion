"""
El usuario proporciona una ruta a un archivo .txt.

Tu programa debe:
1. Abrir el archivo (manejar errores).
2. Contar:
    * Número de líneas
    * Número de palabras
    * Número de caracteres
3. Guardar el reporte en un archivo llamado "reporte.txt"
4. Mostrar el reporte en pantalla.
"""

ruta = input("Ingresa la ruta del archivo .txt que deseas analizar: ")

try:
    # Intentamos abrir y leer el archivo en modo lectura
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Contar líneas, palabras y caracteres
    num_lineas = contenido.count('\n') + 1 if contenido.strip() != "" else 0
    num_palabras = len(contenido.split())
    num_caracteres = len(contenido)

    # Crear reporte en texto
    reporte = (
        f"Reporte del archivo analizado:\n"
        f"Ruta: {ruta}\n\n"
        f"Líneas: {num_lineas}\n"
        f"Palabras: {num_palabras}\n"
        f"Caracteres: {num_caracteres}\n"
    )

    # Guardamos el reporte en un archivo nuevo
    with open("reporte.txt", "w", encoding='utf-8') as rep:
        rep.write(reporte)

    # Mostrar reporte
    print("\n--- REPORTE GENERADO ---")
    print(reporte)
    print("El archivo 'reporte.txt' ha sido creado exitosamente.")

except FileNotFoundError:
    print("Error: El archivo no existe. Verifica la ruta e inténtalo de nuevo.")

except PermissionError:
    print("Error: No tienes permisos para abrir o leer ese archivo.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
