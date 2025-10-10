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


