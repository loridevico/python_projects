import random
from forcaimgs import logo, stages
from forcapal import lista_palavras

#lista_palavras = ["aardvark", "baboon", "camel"]
palavra = random.choice(lista_palavras)
vidas = 6

#print(f'A resposta é {palavra}.')
print(logo)


bls = []
tam = len(palavra)
for _ in range(tam):
    bls += "_"
print(bls)

fim = False

while not fim:
    chute = input("Adivinhe uma letra: ").lower()

    if chute in bls:
      print(f"Você já chutou {chute}")

    for pos in range(tam):
        letra = palavra[pos]
        if letra == chute:
            bls[pos] = letra    
    print(bls)

    if chute not in palavra:
        print(f"{chute} não existe na palavra.")
        vidas -= 1
        if vidas == 0:
            print("Você perdeu!")
            print(f"A palavra era {palavra}")
            fim = True

    print(f"{''.join(bls)}")

    if "_" not in bls:
        fim = True
        print("Parabéns! Você acertou!")
    
    print(stages[vidas])
