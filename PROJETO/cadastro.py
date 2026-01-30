pessoas = []

def cadastrar_pessoa():
    try:
        pessoa = {
            "Nome": input("Digite seu nome: "),
            "Idade": int(input("Digite sua idade: ")),
            "Altura": float(input("Digite sua altura em metros (ex: 1.80): ")),
            "Cidade": input("Digite a cidade em que você mora: ")
        }
        pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!\n")
    except ValueError:
        print("Erro: idade deve ser número inteiro e altura deve ser número.\n")

def listar_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
        return

    print("\nCadastro de Pessoas:")
    for i, pessoa in enumerate(pessoas):
        print(f"{i} - {pessoa['Nome']} tem {pessoa['Idade']} anos, "
              f"mora em {pessoa['Cidade']} e sua altura é {pessoa['Altura']} metros.")

        
def mostrar_pessoas():
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
    else:
        print('Pessoas cadastradas:')
        for pessoa in pessoas:
            print(f"- {pessoa['Nome']}")

def remover_pessoa():
    listar_pessoas()

    try:
        indice = int(input("Digite o número da pessoa que deseja remover: "))

        if 0 <= indice < len(pessoas):
            removida = pessoas.pop(indice)
            print(f"{removida['Nome']} foi removido(a) com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Erro: digite um número válido.")

