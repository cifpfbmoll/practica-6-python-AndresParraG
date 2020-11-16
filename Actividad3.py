lista = []
seguir = True

while seguir:
    a = float(input("Introduce notas entre 0 y 10\n"))
    if (a >= 0.0) and (a <= 10.0):
        lista.append(a)
    else:
        seguir = False

print (lista)