from PROJETO.cadastro import cadastrar_pessoa, listar_pessoas, remover_pessoa

def menu():
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Remover")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        listar_pessoas()
    elif opcao == "3":
        remover_pessoa()
    elif opcao == "0":
        return False
    else:
        print("Opção inválida.")

    return True
