def comparar (lista1, lista2):
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3

lista1 = [1,2,3,'abacaxi']
lista2 = [2,'abacaxi',9,10,'jumento']

print(comparar(lista1,lista2))
