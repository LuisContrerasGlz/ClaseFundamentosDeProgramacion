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

