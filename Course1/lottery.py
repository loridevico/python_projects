#random
#list
#for & while

import random as rd

nums_loteria = []

for i in range(0,6):
    numero = rd.randint(1,50)
    while numero in nums_loteria:
        numero = rd.randint(1,50)
    nums_loteria.append(numero)
nums_loteria.sort()

print(nums_loteria)