# Crea un set con varios números y agrega un nuevo número usando .add().

numeros = {1, 2, 3, 4}
numeros.add(5)

print(numeros)

# Crea dos sets de nombres y muestra la unión, intersección y diferencia.

grupo_A = {"Ana", "Luis", "Pedro", "Marta"}
grupo_B = {"Marta", "Carlos", "Luis"}

print("Unión:", grupo_A | grupo_B)
print("Intersección:", grupo_A & grupo_B)
print("Diferencia (A - B):", grupo_A - grupo_B)

# Convierte una lista con elementos repetidos en un set y muéstralo sin duplicados.

numeros = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = set(numeros)

print(sin_duplicados)

"""
Crea un programa que compare dos listas de alumnos y muestre:

Quiénes están en ambos grupos.

Quiénes están solo en uno.
"""

grupo1 = {"Ana", "Luis", "María", "Pedro"}
grupo2 = {"Luis", "Pedro", "Sofía", "Jorge"}

en_ambos = grupo1 & grupo2
solo_en_uno = grupo1 ^ grupo2

print("En ambos grupos:", en_ambos)
print("Solo en uno:", solo_en_uno)

# Pide palabras al usuario hasta que escriba "fin". Guárdalas en un set e imprímelo al final.

palabras = set()

while True:
    palabra = input("Escribe una palabra ('fin' para terminar): ")
    if palabra == "fin":
        break
    palabras.add(palabra)

print("Palabras únicas:", palabras)

# Pide al usuario una palabra y muestra las letras sin repetir, en el mismo orden en que aparecen.

palabra = input("Ingresa una palabra: ")

letras_vistas = set()
resultado = ""

for letra in palabra:
    if letra not in letras_vistas:
        resultado += letra
        letras_vistas.add(letra)

print("Palabra sin letras repetidas:", resultado)

"""
Tienes tres listas de números con algunos repetidos.
Combínalas en un solo conjunto sin duplicados y muéstralo ordenado.
"""

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
lista3 = [6, 7, 8, 1]

unidos = set(lista1) | set(lista2) | set(lista3)
ordenados = sorted(unidos)

print("Números únicos y ordenados:", ordenados)

# Pide al usuario una frase y muestra cuántas palabras diferentes contiene, ignorando mayúsculas y signos de puntuación.

frase = input("Ingresa una frase: ")

# Convertir todo a minúsculas y limpiar signos
limpia = ""
for c in frase:
    if c.isalpha() or c.isspace():
        limpia += c.lower()

palabras = limpia.split()
palabras_unicas = set(palabras)

print("Palabras únicas:", palabras_unicas)
print("Cantidad de palabras diferentes:", len(palabras_unicas))

