def teste(**kwargs):    
    if 'nome' in kwargs:
        print(f"Nome: {kwargs['nome']}")
    if 'idade' in kwargs:
        print(f"Idade: {kwargs['idade']}")

teste(nome="Ana", idade=25)