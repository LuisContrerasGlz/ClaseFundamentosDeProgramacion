tup = (1, 10, 4, True, "str")

print(tup[1])   # esto muestra 10
print(tup[-1])  # esto muestra "str"

tup[1] = 0      # esto genera una excepción
tup.append(1)   # esto genera una excepción
