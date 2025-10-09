"""

Suma de números hasta cierto límite

Recorre la lista:

lst = [2, 4, 6, 8, 10, 12, 14]

Suma los números hasta que aparezca un 10. Usa break y muestra la suma.

Salida esperada: 20 (2 + 4 + 6 + 8).


"""

lst = [2, 4, 6, 8, 10, 12, 14]

suma = 0
for num in lst:
    if num == 10:
        break
    suma += num

print(suma)  # Salida: 20

"""

Saltando múltiplos de 3

Recorre la lista:

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Imprime todos los números excepto los múltiplos de 3


"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in lst:
    if num % 3 == 0:
        continue
    print(num)

"""

Contar vocales en una cadena

Pide al usuario una palabra y cuenta cuántas vocales (a, e, i, o, u) tiene usando un for.

Si el usuario escribe "python", la salida debe ser:

Número de vocales: 1


"""

s = input("Escribe una palabra: ")
vocales = "aeiou"
contador = 0

for i in s.lower():
    if i in vocales:
        contador += 1

print("Número de vocales:", contador)

"""

Tabla de multiplicar

Usa un bucle for con range para mostrar la tabla de multiplicar del 5, del 1 al 10.

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50



"""

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""

Encontrar el mayor número

Dada la lista:

lst = [15, 22, 8, 35, 19, 50, 41]

Usa un bucle for para recorrer los elementos y encontrar el número más grande (sin usar max()).

Salida esperada:

El mayor número es: 50


"""

lst = [15, 22, 8, 35, 19, 50, 41]

mayor = lst[0]
for num in lst:
    if num > mayor:
        mayor = num

print("El mayor número es:", mayor)  # Salida: 50

