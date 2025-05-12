'''Crie um programa que descubra se uma figura geométrica é um quadrado ou um retângulo:
Um quadrado possui a base e a altura iguais, enquanto um retângulo tem a base e a altura em valores diferentes.'''


base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

if base == altura:
    print("É um quadrado.")
else:
    print("É um retângulo.")
