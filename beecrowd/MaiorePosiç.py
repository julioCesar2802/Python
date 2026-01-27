
lista = []
for i in range (1, 101):
    valor = int(input())
    lista.append(valor)
maior = max(lista)
posicao = lista.index(maior) + 1
print(maior)
print(posicao)