a = list(map(int, input
             ("Digite uma lista de números separados por espaço: ")
             .split()))

def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

maior, menor = maior_menor(a)
print("O maior número é:", maior)
print("O menor número é:", menor)