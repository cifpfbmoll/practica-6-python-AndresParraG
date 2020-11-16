lista = []
seguir = True

while seguir:
    a = input(str("Escriba palabras para una lista\n"))
    if len(a) != 0:
        lista.append(a)
    else:
        seguir = False

print (lista)