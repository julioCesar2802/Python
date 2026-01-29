#REVER O CÓDIGO


a , b = map(int, input().split())

lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

if all(elem in lista1 for elem in lista2):
    print("S")
else:
    print("N")