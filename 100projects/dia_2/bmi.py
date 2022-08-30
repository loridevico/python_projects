import math

altura = float(input("Digite sua altura em metros:"))
peso = float(input("Digite seu peso em kg:"))

bmi = round(peso/(altura**2))
#bmi = peso/(math.pow(altura,2))
print("Seu IMC é:" + bmi)
