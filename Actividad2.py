lista = []
seguir = True

while seguir:
    a = input("Escriba un número para una lista\n")
    if a == 'Salir':
        seguir = False
    else:
        lista.append(a)

print (lista)