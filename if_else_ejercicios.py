"""
1. Número positivo o negativo

Pide un número entero al usuario y muestra si es positivo, negativo o cero.

"""

numero = int(input("Escribe un número: "))

if numero > 0:
    print(f"El número {numero} es positivo")
elif numero < 0:
    print(f"El número {numero} es negativo")
else:
    print("El número es cero")



"""
2. Mayor de edad

Solicita la edad de una persona y muestra un mensaje que indique si es mayor de edad (18 o más) o menor de edad.

"""

edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


"""
3. Par o impar

Solicita un número y muestra si es par o impar.

"""

numero = int(input("Escribe un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")


"""

4. Calificación aprobatoria

Pide una calificación (0–100).

Si es menor a 60, muestra "Reprobado".
Si está entre 60 y 100, muestra "Aprobado".
 

"""

calificacion = int(input("Escribe tu calificación (0-100): "))

if calificacion >= 60:
    print("Aprobado")
else:
    print("Reprobado")

"""
5. Comparar dos números

Solicita dos números y muestra cuál es el mayor o si son iguales.

"""

a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{b} es mayor que {a}")
else:
    print("Ambos números son iguales")


"""
6. Calculadora simple

Solicita dos números y una operación (+, -, *, /).
Usa if-elif-else para mostrar el resultado.

"""

a = float(input("Escribe el primer número: "))
b = float(input("Escribe el segundo número: "))
operacion = input("Elige operación (+, -, *, /): ")

if operacion == "+":
    print(f"{a} + {b} = {a + b}")
elif operacion == "-":
    print(f"{a} - {b} = {a - b}")
elif operacion == "*":
    print(f"{a} * {b} = {a * b}")
elif operacion == "/":
    print(f"{a} / {b} = {a / b}")
else:
    print("Operación no válida")


"""
7. Nota con letras

Pide una calificación de 0 a 100 y muestra la letra según este rango:

90–100 → A
80–89 → B
70–79 → C
60–69 → D
Menor de 60 → F
 
"""

nota = int(input("Escribe tu calificación (0-100): "))

if nota >= 90:
    print("Tu nota es A")
elif nota >= 80:
    print("Tu nota es B")
elif nota >= 70:
    print("Tu nota es C")
elif nota >= 60:
    print("Tu nota es D")
else:
    print("Tu nota es F")



"""

8. Número dentro de un rango

Pide un número y revisa si está dentro del rango 1 a 10.
Muestra un mensaje diferente si está fuera del rango.

"""

num = int(input("Escribe un número: "))

if 1 <= num <= 10:
    print(f"El número {num} está dentro del rango 1-10")
else:
    print(f"El número {num} está fuera del rango")


"""
9. Identificar vocal o consonante

Pide una letra y determina si es una vocal o consonante.


"""

letra = input("Escribe una letra: ").lower()

if letra in "aeiou":
    print(f"La letra {letra} es una vocal")
else:
    print(f"La letra {letra} es una consonante")


"""
10. Conversión de temperatura

Pide una temperatura en Celsius y muestra si está:

Congelada (≤ 0)
Fría (1–15)
Templada (16–30)
Caliente (> 30)
 
"""
c = float(input("Escribe la temperatura en °C: "))

if c <= 0:
    print("Está congelada")
elif c <= 15:
    print("Está fría")
elif c <= 30:
    print("Está templada")
else:
    print("Está caliente")


"""

11. Calculadora de propinas

Pide la cuenta total de un restaurante y evalúa:

Si es menor de 200 → propina del 10%
Si está entre 200 y 500 → propina del 15%
Si es mayor de 500 → propina del 20%
 
"""


"""

12. Piedra, papel o tijeras (versión simple)

Pide a dos jugadores que escriban "piedra", "papel" o "tijeras".
Usa condiciones para determinar quién gana o si es empate.

"""