import random
lista_palavras = ["aardvark", "baboon", "camel"]

palavra = random.choice(lista_palavras)

chute = input("Adivinhe uma letra:").lower()
for l in palavra:
    if chute == l:
        print("Certo")
    else:
        print("Errado")
