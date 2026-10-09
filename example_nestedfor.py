# Usa bucles anidados para imprimir las tablas de multiplicar del 1 al 5.

for i in range(1, 6):        # Tablas del 1 al 5
    for j in range(1, 11):   # Cada tabla hasta el 10
        print(i, "x", j, "=", i * j)