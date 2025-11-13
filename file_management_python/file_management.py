# W mode for write
write_file = open(r'FakeFile.txt', 'w')
write_file.write('This is our first sentence in our file.')
write_file.close()

# A for us to append to the file
append_file = open(r'FakeFile.txt', 'a')
append_file.write(' This is our Second sentence in our file.')
append_file.close()

# Write multi line

multi_line = """
This is the Fourth sentence.
This is the Fifth sentence.
This is the Sixth sentence.
"""

with open(r'FakeFile.txt', 'a') as append_file:
    append_file.write(multi_line)

# Read complete file 

with open(r'FakeFile.txt', 'r') as read_file:
    contenido = read_file.read()
    print(contenido)

# Using try except 

try:
    with open('datos.txt', 'r') as file:
        contenido = file.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print("Error: El archivo no existe. Verifica la ruta.")

except PermissionError:
    print("Error: No tienes permisos para abrir este archivo.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
