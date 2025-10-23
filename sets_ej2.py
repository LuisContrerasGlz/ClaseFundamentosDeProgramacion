# Verificar si una cadena tiene todos los caracteres únicos

texto = input("Ingresa una palabra: ")

if len(set(texto)) == len(texto):
    print("Todos los caracteres son únicos.")
else:
    print("Hay caracteres repetidos.")

# Encontrar la intersección entre dos listas

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

comunes = set(lista1) & set(lista2)

print("Elementos comunes:", comunes)

# Eliminar duplicados de una lista sin usar bucles

numeros = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = list(set(numeros))

print("Lista sin duplicados:", sin_duplicados)
