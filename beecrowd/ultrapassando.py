#(CODIGO IMCOMPLETO)
casos = int(input())
contador = 1
for i in range(casos):
    pa , pb , g1 , g2 = map(float, input().split())
    while pa <= pb:
        pa += pa * (g1 / 100)
        pb += pb * (g2 / 100)
        contador += 1
        if contador > 100:
            print("Mais de 1 seculo.")
            break
    if contador <= 100:
        print(f"{contador} anos.")
    contador = 1

