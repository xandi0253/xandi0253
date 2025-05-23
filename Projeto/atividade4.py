'''Crie um programa que recebe 2 números e diz qual é o maior'''

num1: float = 0
num2: float = 0

num1 = float(input("Digite um número:",))
num2 = float(input("Digite outro número:",))

if num1 > num2: 
    print("O maior número é:", num1)

elif num2 > num1:
    print("O maior número é:", num2)

else:
    print("Os dois números são iguais.")