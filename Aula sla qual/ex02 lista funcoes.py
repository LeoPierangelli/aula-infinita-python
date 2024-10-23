p = 0
lista_de_numeros = []
while p < 5:
    var = input('Insira 5 números para saber qual o maior deles\n->')
    while not (var.isnumeric):
        var = input('Insira um valor válido!\n->')
        break
    var = int(var)
    lista_de_numeros.append(var)
    p += 1

def maior_elemento(parametro):
    maior = parametro[0]
    for i in range(len(parametro)): #pra que esse len?
        if parametro[i] > maior:
            maior = parametro[i]
    return print(maior)

maior_elemento(lista_de_numeros)


