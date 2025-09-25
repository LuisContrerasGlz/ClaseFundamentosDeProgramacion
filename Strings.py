# El tipo de dato str representa una secuencia de caracteres.
#En Python, comienzan y terminan con ", ', """ o '''.

"hello"
"2.0"
'str'
"""False"""
'''true'''

# El carácter de nueva línea es \n.

print("hello\nworld\n!")

# ==========================
# Strings: índices (positivos y negativos)
# ==========================
s = "Python"
print("String:", s)

# Índices positivos:      P   y   t   h   o   n
#                         0   1   2   3   4   5
print("s[0]:", s[0])      # P
print("s[3]:", s[3])      # h

# Índices negativos:      P   y   t   h   o   n
#                        -6  -5  -4  -3  -2  -1
print("s[-1]:", s[-1])    # n
print("s[-3]:", s[-3])    # h

# Slicing (rebanadas) opcional para mostrar rango
print("s[1:4]:", s[1:4])  # yth


# ==========================
# len(): longitud del string
# ==========================
frase = "hola mundo"
print("len(frase):", len(frase))  # 10 (incluye el espacio)


# ==========================
# count(): cuántas veces aparece un substring
# ==========================
texto = "banana"
print("texto:", texto)
print("texto.count('a'):", texto.count('a'))     # 3
print("texto.count('na'):", texto.count('na'))   # 2
print("texto.count('x'):", texto.count('x'))     # 0

# count con rangos (inicio, fin) opcional
print("count('a', 2, 5):", texto.count('a', 2, 5))  # 1 (entre índices 2 y 4)


# ==========================
# find(): posición de la primera ocurrencia
# ==========================
mensaje = "abracadabra"
print("mensaje:", mensaje)

print("mensaje.find('bra'):", mensaje.find('bra'))   # 1
print("mensaje.find('ra'):", mensaje.find('ra'))     # 2
print("mensaje.find('z'):", mensaje.find('z'))       # -1 (no encontrado)

# find con inicio opcional
print("mensaje.find('bra', 2):", mensaje.find('bra', 2))  # 8


# ==========================
# - find() devuelve -1 si no encuentra el substring.
# - count() devuelve cuántas veces aparece (0 si no aparece).
# - En strings no podemos reasignar un carácter: s[0] = 'X' daría error (inmutables).
# ==========================

