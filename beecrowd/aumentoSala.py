salario = float(input())

if salario >= 0 and  salario <= 400:
    aumento = salario * 0.15
    novo = salario + aumento
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print("Em percentual: 15 %")

elif salario > 400 and salario <= 800:
    aumento = salario * 0.12
    novo = salario + aumento
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print("Em percentual: 12 %")

elif salario > 800 and salario <= 1200:
    aumento = salario * 0.10
    novo = salario + aumento
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print("Em percentual: 10 %")

elif salario > 1200 and salario <= 2000:
    aumento = salario * 0.07
    novo = salario + aumento
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print("Em percentual: 7 %")

elif salario > 2000:
    aumento = salario * 0.04
    novo = salario + aumento
    print(f"Novo salario: {novo:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print("Em percentual: 4 %")

