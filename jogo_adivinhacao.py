import random
numero = random.randint(1,10)
jogo = {
    "tentativas": 0,
    "acertou": False
}
while not jogo["acertou"]:
    try:
        t1 = int(input("Digite um numero entre 1 e 10: "))
        jogo["tentativas"] += 1
        
        if t1 == numero:
            print("Paraéns você acertou!")
            jogo["acertou"] = True
        elif t1 < numero:
            print("Numero muito baixo")
        else:
            print("Numero muito Alto")
    except:
        print("Digite um numero valido")

print("tentativas", jogo["tentativas"])
