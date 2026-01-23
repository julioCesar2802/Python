a , b = map(int, input("Digite a largura e comprimento do terreno:").split())

def area(largura, comprimento):
    area = largura * comprimento
    return area

print(f"Área do terreno: {area(a, b)} m²")