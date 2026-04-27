usuario = "admin"
senha = "1234"
lg = {
    "tentativas": 0,
    "login": False
    }
while lg["tentativas"] < 3:
    try:
        u1 = input("Digite o usuario: ")
        s1 = input("Digite a senha: ")
        lg["tentativas"] += 1
        if u1 == usuario and s1 == senha:
            lg["login"] = True
            print("Login bem-sucedido")
            break
        else:
            print("Usuario ou senha incorretos")

        if lg["tentativas"] == 3:
            print("Conta bloqueada")
            break
    except:
        print("erro")
