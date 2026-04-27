pessoa = {
    "nome" : "Heitor",
    "idade" : 16
}
while True:
    print("1 - Ver dados")
    print("2 - Mudar nome")
    print("3 - Mudar idade")
    print("4 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        print("nome: ", pessoa["nome"])
        print("idade: ", pessoa["idade"])
    elif opcao == "2":
        novo_nome = input("Novo nome: ")
        pessoa["nome"] = novo_nome
        print("Nome Atualizado")
    elif opcao == "3":
        nova_idade = int(input("Nova idade: "))
        pessoa["idade"] = nova_idade
        print("Idade Atualizada")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("opçao invalida")
