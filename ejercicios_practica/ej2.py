"""
Palabra más larga

Pide al usuario ingresar una frase.

Usa un bucle para determinar cuál es la palabra más larga de la frase.

"""

# Pedir una frase al usuario
frase = input("Ingresa una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# Suponemos que la primera palabra es la más larga
palabra_mas_larga = palabras[0]

# Recorrer cada palabra y comparar su longitud
for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

# Mostrar el resultado
print("La palabra más larga es:", palabra_mas_larga)

"""

Clasificar números



Pide 10 números y guarda:

 

Los pares en una lista llamada pares.

Los impares en una lista llamada impares

Imprime ambos al final.

"""

pares = []
impares = []

# Pedir 10 números al usuario
for i in range(10):
    num = int(input("Ingresa un número: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar resultados
print("Números pares:", pares)
print("Números impares:", impares)

"""

Contar letras específicas

Pide al usuario una palabra y una letra.

Cuenta cuántas veces aparece esa letra dentro de la palabra.

"""

palabra = input("Ingresa una palabra: ")
letra = input("Ingresa una letra a buscar: ")

contador = 0

for caracter in palabra:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la palabra '{palabra}'.")

"""

Suma de números positivos

Pide al usuario números hasta que escriba 0.

Suma solo los números positivos y muestra el resultado final.


"""

suma = 0

while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        suma += num

print("La suma de los números positivos es:", suma)

# Pide al usuario una frase y muestra cuántas palabras tiene.

frase = input("Ingresa una frase: ")

palabras = frase.split()
cantidad = len(palabras)

print("La frase tiene", cantidad, "palabras.")



"""

- Productos con precio mayor a 50


Crea un diccionario con al menos 20 productos y sus precios.

Imprime solo los productos cuyo precio sea mayor a 50.

"""

productos = {
    "Camisa": 45,
    "Pantalón": 60,
    "Zapatos": 80,
    "Gorra": 30,
    "Reloj": 120
}

print("Productos con precio mayor a 50:")
for nombre, precio in productos.items():
    if precio > 50:
        print(nombre, "→", precio)


