a = int(input("Digite um número"))
contador = 0
lista = []

for i in range(1, a+1):
    if a % i == 0:
        contador += 1
        lista.append(i)

if contador > 2:
            print("Número listado não é primo ")
            print(f"Os números divisiveis por ele são {lista} ")

elif contador == 2:
    print("Número listado é primo")
    print(f"Os números divisiveis por ele são {lista} ")

else:
    print("Número listado não é primo ")
    print(f"Os números divisiveis por ele são {lista} ")                    

    