ano = int(input("Digite o ano a ser checado: "))

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print("O ano é bissexto.")
        else:
            print("Não é bissexto.")
    else:
        print("O ano é bissexto!")
else:
    print("Não é bissexto!")
