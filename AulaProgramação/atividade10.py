'''10. Faça um programa que leia um número, verifique se este número é positivo, negativo
ou Zero. Se for negativo mostre a mensagem "Você digitou um numero negativo", Se for
positivo mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou
zero”.'''

num: float = 0
num = float(input("Digite um número:",))
if num < 0:
    print("Você digitou um número negativo")
elif num > 0:
    print("Você digitou um número positivo")
else:
    print("Você digitou zero")