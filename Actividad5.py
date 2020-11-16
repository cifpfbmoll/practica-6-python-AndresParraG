lista = []
a = 0
b = -1
seguir = True

while seguir:
    a = int(input("Intoduce un número mayor que el anterior: "))
    if a>b:
        lista.append(a)
        b=a
    else:
        seguir = False


print ("Los número que has escrito son: ", end ="")

for i in range(len(lista)):
    print (lista[i], end = ", ")
