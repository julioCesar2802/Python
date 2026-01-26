lista = []
for i in range (1,7):
    a = float(input())
    if a > 0:
        lista.append(a)
        soma = sum(lista)
        media = soma / len(lista)
print(f"{len(lista)} valores positivos")
print(f"{media:.1f}")