
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