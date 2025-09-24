# ==========================
# 1. Lista vacía
# ==========================
lista_vacia = []
print("Lista vacía:", lista_vacia)  # []

# ==========================
# 2. Lista de números
# ==========================
numeros = [10, 20, 30, 40, 50]
print("Lista de números:", numeros)

# ==========================
# 3. Lista de strings
# ==========================
nombres = ["Ana", "Luis", "María", "Carlos"]
print("Lista de strings:", nombres)

# ==========================
# 4. Lista combinada
# ==========================
combinada = [25, "Hola", True, 3.14]
print("Lista combinada:", combinada)

# ==========================
# 5. Lista dentro de listas
# ==========================
listas = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print("Lista dentro de listas:", listas)

# ==========================
# 6. Acceso a elementos por índice
# ==========================
colores = ["rojo", "verde", "azul", "amarillo"]
print("Primer color:", colores[0])   # rojo
print("Tercer color:", colores[2])   # azul

# ==========================
# 7. Longitud de la lista con len()
# ==========================
frutas = ["manzana", "plátano", "naranja"]
print("Número de frutas:", len(frutas))  # 3

# ==========================
# 8. len() en strings
# ==========================
palabra = "Python"
print("Número de caracteres en 'Python':", len(palabra))  # 6

# ==========================
# 9. Cambiar elemento en la lista
# ==========================
animales = ["perro", "gato", "conejo"]
animales[1] = "tigre"
print("Lista modificada:", animales)

# ==========================
# 10. Error al acceder a un índice inexistente
# ==========================
numeros = [1, 2, 3]
# Descomenta la siguiente línea para ver el error
# print(numeros[5])  # IndexError: list index out of range

# ==========================
# 11. Agregar elementos con append()
# ==========================
alumnos = ["Ana", "Luis"]
alumnos.append("María")
print("Lista con append:", alumnos)

# ==========================
# 12. pop(): eliminar y devolver un elemento
# ==========================
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)

# Elimina el último elemento
ultimo = numeros.pop()
print("Elemento eliminado:", ultimo)       # 50
print("Lista después de pop():", numeros)  # [10, 20, 30, 40]

# Elimina por índice
segundo = numeros.pop(1)
print("Elemento en índice 1 eliminado:", segundo)  # 20
print("Lista después de pop(1):", numeros)        # [10, 30, 40]


# ==========================
# 13. count(): contar cuántas veces aparece un valor
# ==========================
letras = ["a", "b", "c", "a", "b", "a"]
print("Lista:", letras)
print("La 'a' aparece:", letras.count("a"), "veces")  # 3
print("La 'b' aparece:", letras.count("b"), "veces")  # 2
print("La 'z' aparece:", letras.count("z"), "veces")  # 0


# ==========================
# 14. index(): obtener la posición de un elemento
# ==========================
colores = ["rojo", "verde", "azul", "amarillo", "verde"]
print("Lista de colores:", colores)

pos_verde = colores.index("verde")
print("Primera posición de 'verde':", pos_verde)  # 1

# Si el elemento no existe, da error:
# print(colores.index("negro"))  # ValueError: 'negro' is not in list


# ==========================
# 15. remove(): eliminar la primera aparición de un valor
# ==========================
animales = ["perro", "gato", "conejo", "gato"]
print("Lista original:", animales)

animales.remove("gato")
print("Después de remove('gato'):", animales)  # ['perro', 'conejo', 'gato']

# Si el valor no existe, da error:
# animales.remove("tigre")  # ValueError: list.remove(x): x not in list
