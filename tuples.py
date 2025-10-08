tup = (1, 10, 4, True, "str")

print(tup[1])   # esto muestra 10
print(tup[-1])  # esto muestra "str"

tup[1] = 0      # esto genera una excepción
tup.append(1)   # esto genera una excepción

# Ejemplo 1: contar elementos en una tupla
x = (1, 2, 3)
count = x.count(1)
print(count)   # salida: 1

# Ejemplo 2: verificar si un elemento está en la tupla
x = (1, 2, 3)
contains = 4 in x
print(contains)   # salida: False

# Ejemplo 3: tupla con diferentes tipos de datos
x = (1, 2, 3, (1, 2), True, [])
print(x)

# Ejemplo 4: acceder a elementos anidados
x = (1, 2, 3, (1, 2), True, [])
print(x[3][0])   # salida: 1

# Ejemplo 5: concatenar tuplas
x = (1, 2)
y = (3, 4)
combined = x + y
print(combined)   # salida: (1, 2, 3, 4)

# Ejemplo 6: repetir elementos de una tupla
combined = (1,) * 10
print(combined)   # salida: (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

# Ejemplo 7: tupla sin paréntesis (packing implícito)
x = 1, 2, 3, 4
print(x)   # salida: (1, 2, 3, 4)

# Ejemplo 8: crear una nueva tupla a partir de otra
x = (1, 2, 3)
y = (x[0], 4, x[2])
print(y)   # salida: (1, 4, 3)

