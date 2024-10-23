def sort_pares(lista_numeros):
    lista_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

fodase = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sort_pares(fodase))
