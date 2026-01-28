a = list(map(int, input("Digite os elementos da lista separados por espaço: ").split()))

def maior_elemento(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

print(f"O maior elemento da lista é: {maior_elemento(a)}")