# ---MEUS EXERCICIOS DE ENUMERATE---
# 1 --Classificação de uma corrida---
atletas = ["Heitor", "Gabriel", "Mariana", "Lucas", "Beatriz"]
for i, nome in enumerate(atletas):
    if i == 0:
        print(f"Ouro: {nome}")
    elif i == 1:
        print(f"Prata: {nome}")
    elif i == 2:
        print(f"Bronze: {nome}")
    else:
        print(f"Participantes: {nome}")

# 2 --Relatório de Estoque--
produtos = ["Teclado", "Mouse", "Monitor", "Cabo HDMI", "Headset"]
estoque = [15, 5, 12, 8, 20]
for i, nome in enumerate(produtos):
    qtd = estoque[i]
    if qtd < 10:
        print(f"[ALERTA] Produto: {nome} | Quantiade: {qtd} Repor Imediatamente!")
    else:
        print(f"Produto: {nome} | Quantidade: {qtd} (Estoque Ok)")
# 3 --Analisando Notas--
alunos = ["Heitor", "Ana", "Bruno", "Carla"]
notas = [9.5, 4.2, 6.0, 8.0]
for i, nome in enumerate(alunos):
    n = notas[i]
    if n >= 7:
        print(f"Aluno(a) {nome} Aprovado(a) com nota: {n} ")
    elif n >= 5:
        print(f"Aluno(a) {nome} Recuperação com nota: {n}")
    else:
        print(f"Aluno(a) {nome} Reprovado(a) com nota: {n}")
