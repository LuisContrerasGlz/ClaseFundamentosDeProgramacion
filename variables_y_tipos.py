# Input

user_name = input("¿Cuál es tu nombre? ")
user_age = int(input("¿Cuál es tu edad? "))
print("Hola " + user_name + "!")
print("Tienes " + str(user_age) + " años")
print("El próximo año tendrás " + str(user_age + 1) + " años")

# fstrings

user_name = input("¿Cuál es tu nombre? ")
user_age = int(input("¿Cuál es tu edad? "))
print(f"Hola {user_name}!")
print(f"Tienes {user_age} años")
print(f"El próximo año tendrás {user_age + 1} años")

# Comentario de una sola línea (Single-line comment)

# Este programa pide el nombre al usuario y lo saluda
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)

# Comentario de múltiples líneas (Multi-line comment)
"""
Este programa pide el nombre al usuario y lo saluda
"""
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)


