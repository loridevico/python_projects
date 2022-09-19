import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z', 'ç', 'Ç']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}', '[', ']', '/']

print("bem-vindo ao gerador de senhas!\n")
letra = int(input("Quantas letras você quer?\n"))
num = int(input("E quantos números?\n"))
simb = int(input("E quantos símbolos\n"))

senha = []
for l in range(1, letra + 1):
    senha.append(random.choice(letras))

for n in range(1, num + 1):
    senha.append(random.choice(numeros))

for s in range(1, simb + 1):
    senha += random.choice(simbolos)

random.shuffle(senha)

senha_final = ""
for char in senha:
    senha_final += char

print(f"Sua nova senha gerada é: {senha_final}")