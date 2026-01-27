n = int(input())

for _ in range(n):
    x = int(input())

    if x == 0:
        print("NULL")
    else:
        if x % 2 == 0:
            tipo = "EVEN"
        else:
            tipo = "ODD"

        if x > 0:
            sinal = "POSITIVE"
        else:
            sinal = "NEGATIVE"

        print(f"{tipo} {sinal}")
