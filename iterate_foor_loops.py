# Iteracion "clasica" sobre una lista
lst = [1, 2, 3, 4, 5, True, False]

for i in range(7):
    print(lst[i])


# Items de mas
lst = [1, 2, 3, 4, 5, True, False,9]

for i in range(7):
    print(lst[i])

# Items de menos
lst = [1, 2, 3, 4, 5]

for i in range(7):
    print(lst[i])

# Usando len para mayor control y flexibilidad

lst = [1, 2, 3, 4, 5, True]

for i in range(len(lst)):
    print(lst[i])

# Iterando por elemento

for element in lst:
    print(element)

# Enumerate para conseguir el indice y el elemento
lst = [1, 2, 3, 4, 5, True]

for i, element in enumerate(lst):
    print(i, element)

# Usando Tuples
tup = (2, 3, 4, "hello", "tim", True)

# Recorrer con range y len()
for i in range(len(tup)):
    element = tup[i]
    print(element)

# Recorrer directamente los elementos
for element in tup:
    print(element)

# Recorrer con índice y valor usando enumerate()
for i, element in enumerate(tup):
    print(i, element)

# Usando Strings

s = "my string"

for i in range(len(s)):
    print(s[i])

s = "my string"

for i in s:
    print(i)




