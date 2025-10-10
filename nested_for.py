# nested for loop 

for i in range(10):
    for j in range(10):
        print(j)

# Visual 

for i in range(3):      # bucle externo (3 veces)
    for j in range(3):  # bucle interno (3 veces)
        print("i =", i, "j =", j)

"""

i = 0 j = 0
i = 0 j = 1
i = 0 j = 2
i = 1 j = 0
i = 1 j = 1
i = 1 j = 2
i = 2 j = 0
i = 2 j = 1
i = 2 j = 2

"""

# 3 nested loops

for i in range(10):
    for j in range(10):
        for w in range(2):
            print(i, j, w)

# Ejemplo mas real con listas

lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

for i in range(len(lst)):
    #Tomando la lista en posicion i para recorrerla despues
    interior_lst = lst[i]

    for j in range(len(interior_lst)):
        print(interior_lst[j])

# Ejemplo usando elementos directamente

lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

# Recorre cada sublista directamente
for interior_lst in lst:  
    # Recorre cada valor de la sublista      
    for elemento in interior_lst:  
        print(elemento)

# Dada la cadena "python programming", recorre cada letra e imprime únicamente las vocales.

st = "python programming"

for char in st:
    if char in "aeiou":
        print(char)


# Usa bucles anidados para imprimir las tablas de multiplicar del 1 al 5.

for i in range(1, 6):        # Tablas del 1 al 5
    for j in range(1, 11):   # Cada tabla hasta el 10
        print(i, "x", j, "=", i * j)


# Usa un for anidado para imprimir un triángulo como este:

"""

*
**
***
****
*****


"""
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


# Genera todas las combinaciones posibles de una letra (A, B, C) con un número (1, 2, 3).
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(letra + str(numero))




