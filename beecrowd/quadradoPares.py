a = int(input())

for i in range(1, a + 1):
    quadrado = i * i
    if quadrado % 2 == 0:
        print(f"{i}^2 = {quadrado}")