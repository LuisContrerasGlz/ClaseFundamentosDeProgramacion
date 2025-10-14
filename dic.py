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



