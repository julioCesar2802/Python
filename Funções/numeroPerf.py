a = int(input("Digite o número desejado:"))

def numero_perfeito(n):
    soma_divisores = 0
    for i in range(1,n):
        if n % i == 0:
            soma_divisores += i
    if soma_divisores == n:
        return True
    else:
        return False
    
print(f"O número {a} é perfeito? {numero_perfeito(a)}")