# Usando indice positivo
frutas = ["manzana", "pera", "uva", "mango", "kiwi"]

print(frutas[1:4])

# Usando indice negativo
frutas = ["manzana", "pera", "uva", "mango", "kiwi"]
print(frutas[-3:-1])

# [n:] Desde n hasta el final

frutas[2:]

# [:n] Desde el inicio hasta n-1

frutas[:3]

# Copiando con [:]
copia = frutas[:]

# Revertir con ::-1

texto = "Python"
print(texto[0:3])   # 'Pyt'
print(texto[-3:])   # 'hon'
print(texto[::-1])  # 'nohtyP'
