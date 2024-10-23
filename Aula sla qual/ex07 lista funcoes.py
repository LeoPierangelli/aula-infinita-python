lista_numeros = [1,2,3,4,5,6,7]
a = 0
lista_aux = []
for e in range(0, len(lista_numeros)-1):
    a = e+1
    if lista_numeros[e] > lista_numeros[a]:
        lista_aux.append(False)
    else:
        lista_aux.append(True)

if False in lista_aux:
    print(False)
else:
    print(True)