x = {"Nome" : input("Digite seu nome: "), "Idade" : int(input("Digite sua idade: ")), 
     "Cidade" : input("Digite sua cidade: ") , 
     "Altura" : int(input("Digite sua altura em cm: "))
     }

print(x["Nome"], "Você mora em", x["Cidade"] ,
        " e sua altura em metros é de :", x["Altura"], "e você tem", x["Idade"], "anos.")
