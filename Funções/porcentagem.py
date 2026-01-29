a , b = map(float, input("Digite o valor total e a porcentagem desejada (separados por espaço): ").split())

def calcular_porcentagem(total, porcentagem):
    porcentagem_calculada = (porcentagem / 100) * total
    return total - porcentagem_calculada

print(f"O valor após descontar {b}% de {a} é: {calcular_porcentagem(a, b)}")