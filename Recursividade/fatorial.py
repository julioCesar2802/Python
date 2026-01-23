a = int(input())

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print(f"O fatorial de {a} é: {fatorial(a)}")