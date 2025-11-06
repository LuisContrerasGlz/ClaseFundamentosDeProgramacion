"""
Crea una función llamada saludo() que no reciba parámetros y solo imprima un mensaje de bienvenida.
Llama a la función varias veces.
"""

def saludo():
    print("¡Bienvenido al programa!")

# Llamadas
saludo()
saludo()

"""
Crea una función llamada presentar(nombre, edad) que reciba dos valores e imprima:
Hola, me llamo [nombre] y tengo [edad] años.

"""

def presentar(nombre, edad):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# Ejemplo de uso
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
presentar(nombre, edad)

