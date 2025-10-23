# Pide al usuario una palabra y muestra las letras sin repetir, en el mismo orden en que aparecen.

# Con set O(1)
palabra = input("Ingresa una palabra: ")

letras_vistas = set()
resultado = ""

# Programacion
for letra in palabra:
    if letra not in letras_vistas:
        resultado += letra
        letras_vistas.add(letra)

print("Palabra sin letras repetidas:", resultado)

# Sin set O(n)

palabra = input("Ingresa una palabra: ")

resultado = ""

for letra in palabra:
    if letra not in resultado:
        resultado += letra

print("Palabra sin letras repetidas:", resultado)
