from cadastro import cadastrar_pessoa, pessoas

while True:
    opcao = input("Digite 1 para cadastrar uma pessoa ou 0 para sair: ")

    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.\n")

print("\nCadastro de Pessoas:")
for pessoa in pessoas:
    print(f"{pessoa['Nome']} tem {pessoa['Idade']} anos, "
          f"mora em {pessoa['Cidade']} e sua altura é {pessoa['Altura']} metros.")

