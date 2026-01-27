a = int(input())
resultados = []
for i in range(1, a + 1):
    b = map(float, input().split())
    calculo = sum([valor * peso for valor, peso in zip(b, [2, 3, 5])]) / 10
    resultados.append(calculo)

for resultado in resultados:
    print(f"{resultado:.1f}")