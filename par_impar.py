# Pedimos un número al usuario
numero = int(input('Escribe un número: '))

# Usamos el operador % para obtener el residuo de la división entre 2
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

