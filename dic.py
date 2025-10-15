ages = {
    "Luis": 30,
    "Alex": 33,
    "Juan": 30
}

print("Alex tiene", ages["Alex"], "años")

# Acceder a los elementos del diccionario

x = {2: "hello", "1": 5}

print(x[2])

print(x["1"])

# Agregar un elemento a un diccionario vacío

x = {}

x["key"] = "value"

print(x)
print(x["key"])

# Modificar el valor de una clave existente

x = {"key": 1}

x["key"] = "value"

print(x["key"])

# Agregar una nueva clave al diccionario

x = {"key": 1}

x["key2"] = "value"

print(x)

# Crear un diccionario usando dict()

x = dict()

x["key2"] = "value"

print(x["key2"])

# Eliminar un elemento de un diccionario

x = {1: 1, 2: 2, 3: 3}

del x[1]

print(x)

# Verificar si una clave existe en un diccionario

x = {1: 1, 2: 2, 3: 3}

contains = 1 in x

print(contains)

# Clave no encontrada

x = {2: 1, 3: 3}

contains = 1 in x

print(contains)

# Obtener todos los valores de un diccionario

x = {2: 1, 3: 3}

values = x.values()

print(values)


# Convertir los valores del diccionario a una lista

x = {2: 1, 3: 3}

values = list(x.values())

print(values[0])

# Obtener las claves de un diccionario

x = {2: 1, 3: 3}

keys = list(x.keys())

print(keys[0])

# Obtener las claves y valores con .items()

x = {2: 1, 3: 3}

items = list(x.items())

print(items)

# Recorrer un diccionario con for usando .items()
x = {2: 1, 3: 3}

for key, value in x.items():
    print("Clave:", key, "→ Valor:", value)

# Contar

x = {2: 1, 3: 3}

print(len(x))

# Usar .get() para obtener un valor o asignar uno por defecto

x = {2: 1, 3: 3}

x[4] = x.get(4, 0) + 1

print(x)

# Contar caracteres en una cadena con un diccionario

characters = {}

string = "hello world"

for char in string:
    characters[char] = characters.get(char, 0) + 1

print(characters)

