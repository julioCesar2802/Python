n = int(input())

listas = list(map(int, input().split()))
soma_total = sum(listas)
h = (soma_total - (n * (n - 1) // 2)) / n
if h != int(h) or h < 0:
    print("-1")
    exit()
h = int(h)
excesso = 0
falta = 0

for i in range(len(listas)):
    ideal = h + i
    atual = listas[i]

    if atual > ideal:
        excesso += atual - ideal
    elif atual < ideal:
        falta += ideal - atual
if excesso != falta:
    print("-1")
else:
    print(excesso)

        
