lista = []
a = int(input("Introduce un número límite: "))
b = 0

while b<a:
    num = int(input("Escribe un valor: "))
    lista.append(num)
    b += num

print ("El límite a superar es", a, "La lista creada es: ", end = "")

for i in range(len(lista)):
    print (lista[i], end = ", ")

print ("Cuya suma es:", b)