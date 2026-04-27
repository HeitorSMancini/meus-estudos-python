#Informações das Pessoas#
pessoas = [
    {"nome": "Heitor", "idade": 16},
    {"nome": "Daniel", "idade": 15},
    {"nome": "Kevin", "idade": 14},
]
#criando opções#
while True:
    print("1 - Adicionar Pessoa")
    print("2 - Listar Pessoas")
    print("3 - Buscar pessoa pelo nome")
    print("4 - Sair")
    opcao = input("Escolha: ").strip()
    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("idade: "))
        pessoa = {
            "nome" : nome,
            "idade" :  idade
        }
        pessoas.append(pessoa)
    elif opcao == "2":
        for pessoa in pessoas:
            print("nome:", pessoa["nome"], "|", "idade:", pessoa["idade"])
    elif opcao == "3":
       encontrou = False
       busca = input("Digite o nome da Pessoa: ")
       for pessoa in pessoas:
           if busca == pessoa["nome"]:
               encontrou = True
               print("nome:", pessoa["nome"], "|", "idade:", pessoa["idade"])
               break
       if encontrou == False:
             print("Nao encontrado!")         
    elif opcao == "4":
        print("Saindo...")
        break
    
