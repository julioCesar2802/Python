b , c = map(int, input("Digite os valores de b e e: ").split())

def potencia(b, c):
    if c == 0:
        return 1
    else:
        return b * potencia(b, c - 1)

print(f"{b} elevado a {c} é: {potencia(b, c)}")