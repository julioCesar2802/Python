a = int(input().split()[1])
h1, m1, s1 = map(int, input().split(" : "))

b = int(input().split()[1])
h2, m2, s2 = map(int, input().split(" : "))

total1 = s1 + m1 * 60 + h1 * 3600 + a * 86400
total2 = s2 + m2 * 60 + h2 * 3600 + b * 86400

total = total2 - total1

dias = total // 86400
total %= 86400
horas = total // 3600
total %= 3600
minutos = total // 60
segundos = total % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
