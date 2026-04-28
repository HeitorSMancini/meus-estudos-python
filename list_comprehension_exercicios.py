# --- MEUS EXERCÍCIOS DE LIST COMPREHENSION ---

# 1. Filtrando números pares de 1 a 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [i for i in numeros if i % 2 == 0]
print(f"Pares: {pares}")

# 2. Aumento de 10% para salários abaixo de 1500
salarios = [1200, 1800, 1400, 2000, 1100]
novos_salarios = [i * 1.1 for i in salarios if i < 1500]
print(f"Salários reajustados: {novos_salarios}")

# 3. Limpeza completa de nomes (Espaços, Maiúsculas e Tamanho)
usuarios = [" heitor", "ana", "  JOÃO ", "caio", " bEATRIZ  "]
nomes_limpos = [nome.strip().title() for nome in usuarios if len(nome.strip()) > 3]
print(f"Nomes limpos: {nomes_limpos}")
