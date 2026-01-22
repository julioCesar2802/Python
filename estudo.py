a , b , c , d = map(int,input().split())

if a > c and b > d:
    horas = (c - a)
    minutos = (b - d)
    print (f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

elif a and b and c == d:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")


