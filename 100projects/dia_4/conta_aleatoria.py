import random

nomes = input("Digite o nome das pessoas, separado por vírgulas: ")
nomes_sorteio = nomes.split(", ")
print(nomes_sorteio)

sorteio = random.randint(0,len(nomes_sorteio) - 1)
pagador = nomes_sorteio[sorteio]
print("Quem pagará a conta será " + pagador)