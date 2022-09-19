altura_alunos = input("Digite uma lista de alturas separadas por espaços: ").split()
for n in range(0, len(altura_alunos)):
  altura_alunos[n] = float(altura_alunos[n])

a = len(altura_alunos)
soma = 0
for i in altura_alunos:
    soma = soma + altura_alunos[i]

""" soma = sum(altura_alunos) """

res = soma/a
print(res)