print("Bem-vindo a calculadora de gorjeta!")
conta = float(input("Qual o valor da conta? (Em reais)"))
pessoas = int(input("Quantas pessoas vão pagar?"))
porcen = int(input("Quanto de gorjeta será pago? 10, 15 ou 20?"))

porcentagem = porcen/100
total = conta + conta*porcentagem
por_pessoa = total/pessoas
res = round(por_pessoa,2)
print(res)