import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

tipos = [pedra, papel, tesoura]
usuario = int(input("Vamos jogar! Esclha 0 para Pedra, 1 para Papel e 2 para Tesoura: "))

if usuario > 2 or usuario < 0:
    print("Valor inválido!")
else:
    print(tipos[usuario])
    ia = random.randint(0,2)
    print("O Computador escolheu:")
    print(tipos[ia])

    if usuario == 0 and ia == 2:
        print("Você ganhou!")
    elif usuario == 2 and ia == 0:
        print("Você perdeu!")
    elif usuario > ia:
        print("Você venceu!")
    elif ia > usuario:
        print("Você perdeu!")
    elif usuario == ia:
        print("Empatou!")