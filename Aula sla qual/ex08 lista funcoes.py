'''listapra_la = [1,2,3,4,5,6,7,8,9,10]
listapra_ca = []


for i in range(len(listapra_la)-1,-1,-1):
    listapra_ca.append(listapra_la[i])
print(listapra_ca)'''

lista = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lista)//2):
    aux = lista[i]
    lista[i] = lista[len(lista) - 1 - i]
    lista[len(lista) - 1 - i] = aux

print(lista)
