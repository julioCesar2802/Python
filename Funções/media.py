a = list(map(int, input
             ("Digite uma lista de números separados por espaço: ").split()))

def media(lista):
    soma = sum(lista)
    quantidade = len(lista)
    return soma / quantidade

resultado = media(a)
print("A média dos números é:", resultado)