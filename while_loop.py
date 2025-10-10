num = input("Enter an integer: ")

while not num.isdigit():
    num = input("Enter an integer: ")


# Comparacion de For Loop y While loop

x = 0
while x < 5:
    print(x)
    x += 1

for x in range(5):
    print(x)

# Uso de break
while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        break

lst = [2, 3, 3, 2, 2, 1]

result = 0
i = 0

# Mientras la suma acumulada (result) sea menor que 9
while result < 9:
    # Tomamos el elemento actual de la lista
    num = lst[i]      
    # Lo sumamos al acumulador     
    result += num   
    # Pasamos al siguiente índice       
    i += 1   
    # Imprimimos              
    print(num)

# Si no hay numeros que coincidan

lst = [2, 3, 3, -2, -2, -1]

result = 0
i = 0

# El bucle se ejecuta mientras la suma acumulada (result) sea menor que 9
# Y mientras no se haya llegado al final de la lista
while result < 9 and i < len(lst):
    # Tomamos el elemento actual de la lista
    num = lst[i]    
    # Lo sumamos al acumulador      
    result += num       
    # Pasamos al siguiente índice  
    i += 1  
    # Imprimimos el número procesado en esta iteración             
    print(num)            



