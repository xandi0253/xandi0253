'''12- Faça um programa que leia dois números e efetua a adição. Se o valor somado for
maior que 20, este deverá ser apresentado somando-se a ele 8; se o valor somado for
menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

num1: float = 0
num2: float = 0
num1 = float(input("Digite um número:",))
num2 = float(input("Digite outro número:",))
soma = num1 + num2
if soma > 20:
    soma = soma + 8
    print("O resultado da soma é:", soma)
elif soma <=20:
    soma = soma - 5
    print("O resultado da soma é:", soma)
else:
    print("Os dois números são iguais.")

    