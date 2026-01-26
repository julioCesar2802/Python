a = int(input())
contador = 0
contador1 = 0
for i in range(1,a + 1):
    b = int(input())
    if b >= 10 and b <= 20:
        contador += 1
    else:
        contador1 += 1

print(f"{contador} in")
print(f"{contador1} out")