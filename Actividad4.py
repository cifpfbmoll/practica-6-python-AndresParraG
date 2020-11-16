a = 0
b = 0

a = int(input("Introduce un valor\n"))
b = int(input("Introduce un valor que sea mayor que el anterior\n"))

while a>b:
    print (b, "no es mayor que", a, "Introduce otro número: ")
    b = int(input())

print (b, "es mayor o igual que", a)
