n = int(input())

maior_nota = -1
matricula_maior = None

for i in range(n):
    matricula, nota = map(float, input().split())

    if nota > maior_nota:
        maior_nota = nota
        matricula_maior = int(matricula)

if maior_nota < 8:
    print("Minimum note not reached")
else:
    print(matricula_maior)
