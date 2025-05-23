'''9-  Faça um programa que leia um número, verifique se este número é positivo ou
negativo. Se for negativo mostre a mensagem "Você digitou um numero negativo", Senão
mostre:" Voce digitou um número positivo.
'''

num: float = 0
num = float(input("Digite um número:",))
if num < 0:
    print("Você digitou um número negativo")
elif num > 0:
    print("Você digitou um número positivo")
else:
    print("Você digitou zero")
