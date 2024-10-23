def verifica_inputint(msg):
    num = input(msg)
    while not num.isnumeric():
        print('Inválido!')
        num = input(msg)
    num = int(num)
    return num

def maior_elemento(parametro):
    maior = parametro[0]
    for i in range(len(parametro)): #pra que esse len?
        if parametro[i] > maior:
            maior = parametro[i]
    return print(maior)

p = 0
lista_de_numeros = []
while p < 5:
    var = verifica_inputint('Insira 5 números para descobrir o maior entre eles\n->')
    lista_de_numeros.append(var)
    p += 1

maior_elemento(lista_de_numeros)


