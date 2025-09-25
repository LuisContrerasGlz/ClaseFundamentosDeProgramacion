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

# ==========================
# upper(): convierte a mayúsculas
# ==========================
texto = "Hola Mundo"
print("Texto original:", texto)

mayusculas = texto.upper()
print("Texto en mayúsculas:", mayusculas)  # HOLA MUNDO


# ==========================
# lower(): convierte a minúsculas
# ==========================
frase = "PYTHON es GENIAL"
print("Frase original:", frase)

minusculas = frase.lower()
print("Frase en minúsculas:", minusculas)  # python es genial


# ==========================
# Uso combinado de upper() y lower()
# ==========================
palabra = "pYtHon"
print("Palabra original:", palabra)
print("Solo mayúsculas:", palabra.upper())  # PYTHON
print("Solo minúsculas:", palabra.lower())  # python

# Explicacion de utilidad ejemplo de upper y lower

answer = input("What is my name? ")

if answer == "Luis":
    print("Correct")
else:
    print("Incorrect")

# El codigo arriba fallaria si escribimos luis, LUIS, etc

# Para solucionarlo usamos las funciones

answer = input("What is my name? ")

if answer.lower() == "luis":
    print("Correct")
else:
    print("Incorrect")

# ==========================
# capitalize(): primera letra en mayúscula
# ==========================
texto1 = "python es genial"
texto2 = "hOLa MUNDo"

print("Texto original:", texto1)
print("Con capitalize():", texto1.capitalize())  # Python es genial

print("Texto original:", texto2)
print("Con capitalize():", texto2.capitalize())  # Hola mundo

# ==========================
# strip(): eliminar espacios al inicio y al final
# ==========================
texto = "   hola mundo   "
print("Texto original:", repr(texto))     # '   hola mundo   '
print("Con strip():", repr(texto.strip()))  # 'hola mundo'

# También se puede usar para quitar caracteres específicos
ejemplo = "----Python----"
print("Con strip('-'):", ejemplo.strip("-"))  # Python

# ==========================
# Uso de 'in' en strings
# ==========================

texto = "Python es genial"

# Revisar si un carácter está en el string
print("'P' in texto:", 'P' in texto)      # True
print("'z' in texto:", 'z' in texto)      # False

# Revisar si una palabra está en el string
print("'genial' in texto:", 'genial' in texto)  # True
print("'java' in texto:", 'java' in texto)      # False

# También funciona con condiciones if
if "Python" in texto:
    print("La palabra 'Python' está en el texto")

if "Java" not in texto:
    print("La palabra 'Java' NO está en el texto")

# ==========================
# isdigit(): True si todos los caracteres son dígitos
# ==========================

s = "19"

is_digit = s.isdigit()
print(is_digit)   # True

# ==========================
# isdigit(): False si el string contiene algo distinto a dígitos
# ==========================

s = "19h"

is_digit = s.isdigit()
print(is_digit)   # False

# ==========================
# isdigit() con un número decimal
# ==========================

s = "19.4"

is_digit = s.isdigit()
print(is_digit)   # False

# ==========================
# Ejemplo práctico de isdigit()
# ==========================

num = input("Number: ")

if num.isdigit():
    print("It is a number")
    num = int(num)           # Convertimos el string a entero
    print(num + 5)           # Operación matemática
else:
    print("This is not an int")

# ==========================
# split(): separar un string en una lista de palabras
# ==========================

s = "hello my name is luis"

words = s.split()   # divide el string por espacios
print(words)        # ['hello', 'my', 'name', 'is', 'luis']

# ==========================
# split() con separador personalizado
# ==========================

s = "manzana,pera,uva,melon"

# Usamos split(",") para dividir por comas
frutas = s.split(",")
print(frutas)   # ['manzana', 'pera', 'uva', 'melon']

# Cuando no pasamos nada a split(), se usa el espacio como separador.

# Si queremos usar otro separador (coma, punto, guion, etc.), lo ponemos entre comillas dentro de los paréntesis.

s = "rojo-azul-verde-amarillo"
colores = s.split("-")
print(colores)   # ['rojo', 'azul', 'verde', 'amarillo']

# ==========================
# replace(): reemplazar caracteres o cadenas en un string
# ==========================

s = "hello,my,name,is,,,luis"

# Reemplazar las comas por barras verticales
s2 = s.replace(",", "|")

print(s2)   # hello|my|name|is|||luis
print(s)    # hello,my,name,is,,,luis  (el string original no cambia)

# Otro ejemplo

texto = "python es divertido"
nuevo = texto.replace("divertido", "poderoso")
print(nuevo)   # python es poderoso

# ==========================
# f-strings: interpolación de variables en un string
# ==========================

# Variables
nombre = "Luis"
edad = 25

# Forma tradicional (concatenación)
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

# Usando f-strings (más limpio y legible)
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")









