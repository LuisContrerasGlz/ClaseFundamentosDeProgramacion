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
