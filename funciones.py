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

# Crea una función sumar(a, b) que devuelva la suma de dos números.

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma es {resultado}")

# Crea una función promedio(num1, num2, num3) que devuelva el promedio de tres números.

def promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

resultado = promedio(8, 6, 10)
print(f"El promedio es {round(resultado, 2)}")
