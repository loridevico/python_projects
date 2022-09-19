pontuacoes = input("Digite uma lista de pontuações separadas por espaços: ").split()
for n in range(0, len(pontuacoes)):
  pontuacoes[n] = int(pontuacoes[n])

maior = 0
for i in pontuacoes:
    if i > maior:
        maior = i

print(f"A maior pontuação é de {maior}")