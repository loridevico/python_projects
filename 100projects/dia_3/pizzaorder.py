print("Bem-vindo a Python Pizza!")
tam = input("Que tamanho você deseja? P, M, ou G? ")
add_pepperoni = input("Quer pepperoni? S ou N ")
extra = input("Aceita queijo extra? S ou N? ")

#Pequena: 15.00
#Media: 20.00
#Grande: 25.00

#Pepper p/ pequena: + 2.00
#Pepper p/ media ou grande: + 3.00

#Extra: + 1

conta = 0

if tam == 'P':
    conta = conta + 15
elif tam == 'M':
    conta = conta + 20
else:
    conta = conta + 25

if add_pepperoni == 'S':
    if tam == 'P':
        conta += 2
    else:
        conta += 3

if extra == 'Y':
    conta += 1

print(f"Sua conta é de R${conta}")