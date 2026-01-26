a = int(input())
b = int(input())
menor = min(a , b)
maior = max(a , b)
soma = 0
lista = []
for i in range (menor + 1, maior):
    if i % 2 != 0:
        lista.append(i)
        soma = sum(lista)

print(soma)