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

"""
Crea una función saludar(nombre="invitado") que muestre un saludo.
Si el usuario no escribe un nombre, usa el valor por defecto.
"""

def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

saludar()
saludar("Luis")

"""
Crea una función datos(nombre, edad, ciudad) y haz tres llamadas:

Con argumentos por posición.

Con argumentos por nombre.

Mezclando ambos.
"""

def datos(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Por posición
datos("Ana", 20, "Puebla")

# Por nombre
datos(nombre="Luis", edad=25, ciudad="CDMX")

# Mezclado
datos("María", edad=30, ciudad="Guadalajara")

"""
Crea una función area_triangulo(base, altura) que devuelva el área.
Usa return y muestra el resultado.
"""

def area_triangulo(base, altura):
    return (base * altura) / 2

print(f"El área es {area_triangulo(6, 4)}")

"""
Crea una función celsius_a_fahrenheit(c) que devuelva el valor convertido a Fahrenheit.
Usa la fórmula: F = (C * 9/5) + 32
"""

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

print(f"20°C equivalen a {celsius_a_fahrenheit(20)}°F")

"""
Crea un programa con tres funciones:

menu() – muestra opciones.

suma(a, b) – devuelve la suma.

resta(a, b) – devuelve la resta.

Permite al usuario elegir qué operación realizar.
"""

def menu():
    print("1. Sumar")
    print("2. Restar")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

menu()
opcion = int(input("Elige una opción: "))
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

if opcion == 1:
    print(f"Resultado: {suma(a, b)}")
elif opcion == 2:
    print(f"Resultado: {resta(a, b)}")
else:
    print("Opción no válida.")
