a = int(input())

if a >= 365:
    anos = a // 365
    meses = (a % 365) // 30
    dias = (a % 365) % 30
else:
    anos = 0
    if a >= 30:
        meses = a // 30
        dias = a % 30
    else:
        anos = 0
        meses = 0
        dias = a

print (f"{int(anos)} ano(s)")
print (f"{int(meses)} mes(es)")
print (f"{int(dias)} dia(s)")