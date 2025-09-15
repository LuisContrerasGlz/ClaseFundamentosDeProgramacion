# Condicionales en Python, ejercicios y explicacion

x = 5

if x > 0:
    print("x es mayor que 0")
elif x > 10:
    print("x es mayor que 10")
else:
    print("x es menor o igual a 0")

#El ejemplo anterior tiene una "trampa" para revisar la logica 

"""
Crea un programa en Python que capture la venta de un artículo en una tienda.

El programa debe:

Pedir la descripción del artículo.

Pedir el precio unitario.

Pedir la cantidad de artículos.

Preguntar si el artículo causa IVA (S/N).

Calcular:

Subtotal = precio × cantidad

Descuento según la cantidad:

5 a 10 artículos → 10%

11 a 20 artículos → 20%

Más de 20 artículos → 30%

De 1 a 4 artículos → sin descuento

Base después del descuento

IVA (16%) si aplica

Total del artículo

Mostrar en pantalla: descripción, subtotal, descuento, base después de descuento, IVA y total.


"""

# Captura de un artículo en una venta

descripcion = input("Descripción del artículo: ")
precio = float(input("Precio unitario: $"))
cantidad = int(input("Cantidad: "))
causa_iva = input("¿Causa IVA? (S/N): ")

# Subtotal
subtotal = precio * cantidad

# Descuento según la cantidad
if 5 <= cantidad <= 10:
    descuento = subtotal * 0.10
elif 11 <= cantidad <= 20:
    descuento = subtotal * 0.20
elif cantidad > 20:
    descuento = subtotal * 0.30
else:
    descuento = 0

# Base después del descuento
base = subtotal - descuento

# IVA si aplica
if causa_iva.lower() == "s":
    iva = base * 0.16
else:
    iva = 0

# Total
total = base + iva

# Mostrar resultados
print("\n--- RESULTADO DE LA VENTA ---")
print(f"Artículo: {descripcion}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Base después de descuento: ${base:.2f}")
print(f"IVA: ${iva:.2f}")
print(f"TOTAL: ${total:.2f}")

