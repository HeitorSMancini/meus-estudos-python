compras = ["arroz", "feijao", "batata", "carne", "cenoura"]
def adicionar_item(lista):
    item = input("Digite um item: ")
    lista.append(item)
def remover_item(lista):
 item = input("Digite um item: ")
 if item in lista:
     lista.remove(item)
 else:
     print("Item nao encontrado")
def listar_itens(lista):
    for item in lista:
        print(item)
while True :
 print("1- adicionar")
 print("2- remover")
 print("3- listar")
 print("4- sair") 
 opcao = input("Escolha: ") 
 if opcao == "1":
    adicionar_item(compras)
    print(compras)
 elif opcao == "2":
    remover_item(compras)
    print(compras)
 elif opcao == "3":
    listar_itens(compras)
 elif opcao == "4":
    print("saindo...")
    break
 else:
    print("Opção Invalida")
