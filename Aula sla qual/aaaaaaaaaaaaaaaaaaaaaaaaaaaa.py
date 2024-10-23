def forca_opcao(msg, lista_opcoes):
    opcao = input(msg)
    while not opcao in lista_opcoes:
        print('Inválido!')
        opcao = input(msg)
    return opcao

vinhos = ['pérgola', 'chapinha', 'sangue de boi']
escolha = forca_opcao('Qual vinho você quer? ', vinhos)
