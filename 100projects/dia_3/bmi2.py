altura = float(input("Digite sua altura em metros:"))
peso = float(input("Digite seu peso em kg:"))

bmi = round(peso/(altura**2))
#bmi = peso/(math.pow(altura,2))
print(f"Seu IMC é {bmi}.")
if bmi < 18.5:
    print("Você está abaixo do peso.")
elif bmi < 25:
    print("Você está com o peso normal.")
elif bmi < 30:
    print("Você está com sobrepeso.")
elif bmi < 35:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")


