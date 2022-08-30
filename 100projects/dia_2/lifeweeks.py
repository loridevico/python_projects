idade = int(input("Qual sua idade?"))

tempo = 90 - idade
dias = tempo * 365
semanas = tempo * 52
meses = tempo * 12

res = f"Voce ainda tem {dias} dias, {semanas} semanas e {meses} meses até os 90 anos"
print(res)