"""
Escribe un programa que pida al usuario ingresar cinco cadenas de texto y las almacene en una lista.

Luego, el programa debe pedir al usuario ingresar tres números en el rango de 0 a 4 (incluidos). Estos números representarán índices de la lista.

Finalmente, el programa debe usar esos tres números para acceder a las tres cadenas en los índices correspondientes de la lista previamente creada, concatenarlas y mostrar la cadena resultante en pantalla.

"""

# ==========================
# Programa: concatenar strings usando índices
# ==========================

# Pedir 5 strings y guardarlos en una lista
string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")
string4 = input("Enter a string: ")
string5 = input("Enter a string: ")

strings = [string1, string2, string3, string4, string5]

# Pedir 3 números (índices)
num1 = int(input("Enter a number (0-4): "))
num2 = int(input("Enter a number (0-4): "))
num3 = int(input("Enter a number (0-4): "))

# Concatenar las cadenas en esas posiciones
final_string = strings[num1] + strings[num2] + strings[num3]

# Mostrar resultado
print("Resultado final:", final_string)
