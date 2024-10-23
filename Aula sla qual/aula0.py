'''professores = ['Caio', 'Danilo', 'Caio2', 'Luciano', 'André', 'Yan']
adjetivos = ['1', 'Thor', '2', 'Maromba', 'Maluco', 'Calmo']
for i in range(len(professores)):
    print(f'O {professores[i]} é {adjetivos[i]}')
'''
aux = 0
valores = [50, 70, 10, 10, 20]
maior = valores[0]
for i in range(len(valores)):
    if valores[i] > maior:
        aux = maior
        maior = valores[i]
        valores[i] = aux
print(maior)

'''
def media_notas(notas):
    soma = 0
    for num in notas:
        soma += num
    media = soma/len(notas)
    return media

lista = [3, 8, 5, 9, 10, 9, 7, 2]
media = media_notas(lista)
print(media)
lista_02 = [1,2,3,4,5,6,7]
media = media_notas(lista_02)
print(media)
'''








