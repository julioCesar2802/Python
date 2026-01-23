palavra = str(input("Digite a palavra desejada: "))

def inverso(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + inverso(s[:-1])
    
print(f"A palavra invertida é: {inverso(palavra)}")