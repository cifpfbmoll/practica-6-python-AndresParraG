lista = []
a = int(input("Inroduce el número inferior: "))
b = int(input("Introduce el número superior: "))
seguir = True

print ("Introduce un números entre", a, "y", b + ":")

while seguir:
    c = int(input())
    if c>a and c<b:
        lista.append(c)
    else:
        seguir = False

print ("Los números entre", a, "y", b, "son: ", end = "")

for i in range(len(lista)):
    print (lista[i], end =", ")