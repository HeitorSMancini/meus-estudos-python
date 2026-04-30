# ---EXERCICIO SOBRE MAP---
# 1 --CONVERTENDO TEMPERATURA--
def F(x):
    return (x * 1.8)+ 32
celsius_temps = [0, 10, 20, 30, 40, -5]

fahrenheit = list(map(F, celsius_temps))
print(f"sem lambda: {fahrenheit}")
#Aplicando o uso do LAMBDA#
celsius = [0, 10, 20, 30, 40, -5]
fahrenheit2 = list(map(lambda x: (x * 1.8) +32, celsius))
print(f"com lambda: {fahrenheit2},")
# 2 --PADRONIZAÇÃO DE NOMES--
usuarios = ["  alice ", "BOB", " caio", "DaNiElA "]
padrao = list(map(lambda x: x.strip().capitalize(), usuarios))
print(padrao)
# 3 --CALCULOS DE IMPOSTOS (OU GORJETAS)--
contas = [100, 250, 40, 500]
gorjetas = list(map(lambda x: x * 0.1, contas))
print(gorjetas)
