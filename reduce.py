# ---EXERCICIOS COM USO DE REDUCE
# 1--Total de vendas--
from functools import reduce
vendas = [120.50, 500.00, 89.90, 20.00, 150.00]

item_atual = reduce(lambda x, y: x+y, vendas)
print(f"O total de vendas é: {item_atual}")
print("-"*32)
# 2 --Encontrando maior valor--
precos = [45, 12, 89, 34, 102, 67]
maior = reduce(lambda x, y: x if x > y else y, precos)
print(f"Esse é o maior valor: {maior}")
print("-"*32)
# 3 --Formatador de strings--
partes = ["projeto", "automacao", "python", "v1"]
maiusculo = map(lambda x: x.capitalize(), partes)
junto = reduce(lambda x, y: f"{x}-{y}", partes )
print(junto)
