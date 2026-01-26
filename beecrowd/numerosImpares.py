a = int(input())
contador = 0

numero_atual = a

while contador < 6:
    if  numero_atual % 2 != 0:
        print(numero_atual)
        contador += 1
    numero_atual += 1
