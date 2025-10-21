# Puedes crear un conjunto vacío o con elementos:

# Conjunto vacío
my_set = set()

# Conjunto con valores
my_set = {1, 2, 3, 4, 5}

print(my_set)

# Agregar elementos

my_set = {1, 2, 3}
my_set.add(4)

print(my_set)

# Elimar elementos

my_set = {1, 2, 3, 4}
my_set.remove(2)

print(my_set)

# Verificar si un elemento está en el set

my_set = {1, 2, 3, 4}

print(3 in my_set)   # True
print(5 in my_set)   # False

# Recorrer un set con un bucle for(orden no garantizado)

my_set = {"manzana", "pera", "uva"}

for fruta in my_set:
    print(fruta)

