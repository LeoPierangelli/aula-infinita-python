'''def selecionar (msg,lista_strings):
    p = 0
    while p < 3:
        string = input(msg)
        lista_strings.append(string)
        p += 1
    return lista_strings

palavras = []
selecionar('Digite uma string para adicionar à lista\n->', palavras)
'''
def sort_a(lista_palavras):
    lista_a = []
    for e in lista_palavras:
        if 'a' in e[0]:
            lista_a.append(e)
    return lista_a


askldja = ['abacate', 'abacaxi', 'uva']
print(sort_a(askldja))
