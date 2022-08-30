print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem-vindo a Ilha do Tesouro!")
print("Sua missão é encontrar o tesouro.")
dir = input("Você chegou em uma encruzilhada. Para onde ir? igite 'direita' ou 'esquerda': \n").lower()
if dir == "direita":
    caminho = input("Você chega em um lago. No meio, há uma ilha. Escolha 'esperar' para aguardar o barco ou 'nadar' para ir até lá: \n").lower()
    if caminho == "esperar":
        porta = input("Você chegou ileso, mas encontrou uma casa com três portas: 'azul', 'amarelo', e 'verde'. Qual você escolhe? \n").lower()
        if porta == "azul":
            print("Parabéns! Você encontrou o tesouro!")
        elif porta == "amarelo":
            print("A sala está em chamas. Fim de jogo!")
        elif porta == "verde":
            print("Sala vazia. Fim de jogo!")
        else:
            print("Escolha inválida. Fim de jogo!")
    else:
        print("Você foi atacado por um polvo gigante. Fim de jogo!")
else:
    print("Sem saída. Fim de jogo!")

