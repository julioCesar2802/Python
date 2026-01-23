p , n = map(int, input().split())
lista = list(map(int, input().split()))

for i in range(len(lista) - 1):
    if lista[i + 1] - lista[i] > p or lista[i] - lista[i + 1] > p:
        print("GAME OVER")
        break
else:
    print("YOU WIN")




