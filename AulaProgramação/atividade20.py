"""MAIOR DE TRÊS NÚMEROS: DESENVOLVA UM PROGRAMA QUE RECEBA TRÊS NÚMEROS E DETERMINE 
QUAL É O MAIOR USANDO IF-ELSE"""

num1: float = input("Digite um primeiro número:",)
num2: float = input("Digite um segundo número:",)
num3: float = input("Digite um terceiro número:",)

if num1 > num2:
    print(num1)
elif num2 > num3:
    print(num2)
elif num3 > num1:
    print(num3)


"""Questão de prova(cursinhos)

aux: int = 0
contador: int = 0

while contador < 3:
    num: int = int(input("Informe o numero: "))
    """