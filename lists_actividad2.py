"""
Pide al usuario 5 nombres y guárdalos en una lista llamada nombres.

Muestra en pantalla:

El primer y el último nombre usando índices.

La longitud de la lista con len().

Pide un nombre a eliminar y quítalo de la lista con .remove().

Pide un nombre para agregar y añádelo al final con .append().

Pide un nombre a contar y muestra cuántas veces aparece en la lista con .count().

Pide dos índices (en el rango válido) y concatena los nombres en esas posiciones. Imprime el resultado final.

"""

# ==========================
# Actividad: Agenda de nombres
# ==========================

# 1) Captura de 5 nombres
nombres = []
for i in range(5):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    nombres.append(nombre)

# 2) Mostrar primero, último y longitud
print("Primer nombre:", nombres[0])
print("Último nombre:", nombres[-1])
print("Total de nombres:", len(nombres))

# 3) Eliminar un nombre
a_eliminar = input("Nombre a eliminar: ")
nombres.remove(a_eliminar)

# 4) Agregar un nombre
a_agregar = input("Nombre a agregar: ")
nombres.append(a_agregar)

print("Lista actual:", nombres)

# 5) Contar un nombre
a_contar = input("Nombre a contar: ")
print("El nombre aparece", nombres.count(a_contar), "veces.")

# 6) Concatenar dos nombres por índice
i1 = int(input("Índice 1 (0 a 4): "))
i2 = int(input("Índice 2 (0 a 4): "))
resultado = nombres[i1] + nombres[i2]
print("Concatenación:", resultado)
