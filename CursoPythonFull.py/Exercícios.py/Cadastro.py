# faça um programa que cadastre n pessoas
# armazene seu nome,idade,altura e cidade em que mora

pessoas = []

while True:
    opcao = input("Digite 1 para cadastrar uma nova pessoa ou 0 para sair: ")
    
    if opcao == "1":
        pessoa = {"Nome" : input("Digite seu nome: "),
                  "Idade" : int(input("Digite sua idade: ")),
                  "Altura" : float(input("Digite sua altura em metros,usando por exemplo (1.80): ")),
                  "Cidade" : input("Digite a cidade em que você mora: ")}
        pessoas.append(pessoa)
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")

print("\nCadastro de Pessoas:")
for pessoa in pessoas:
    print(f"{pessoa['Nome']} tem {pessoa['Idade']} anos, "
          f"mora em {pessoa['Cidade']} e sua altura é {pessoa['Altura']} metros.")