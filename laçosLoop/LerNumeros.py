a = int(input("Digite um número: "))
lista = []
while a != 0:
    lista.append(a)
    a = int(input("Digite o próximo número: "))
    if a == 0:
        sum(lista)
        resultado = sum(lista)
        calculo = resultado / len(lista)
        print(f"Média dos números digitados: {int(calculo)}")

