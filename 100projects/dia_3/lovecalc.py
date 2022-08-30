nome1 = input("Digite o seu nome:").lower()
nome2 = input("Digite o nome do seu amor:").lower()

nomes = nome1 + nome2

ts = nomes.count("t")
rs = nomes.count("r")
us = nomes.count("u")
es = nomes.count("e")

true = ts + rs + us + es
print(f"Total = {true}")

ls = nomes.count("l")
os = nomes.count("o")
vs = nomes.count("v")
es2 = nomes.count("e")

love = ls + os + vs + es2 
print(f"Total 2 = {love}")

res = str(true) + str(love)
res_int = int(res)

if res_int < 10 or res_int > 90:
    print(f"Seu resultado é {res_int} e vocês são uma combinação perigosa.")
elif res_int >= 40 and res_int <= 50:
    print(f"Seu resultado é {res_int} e vocês são uma combinação ok.")
else:
    print(f"Seu resultado é {res_int}.")


