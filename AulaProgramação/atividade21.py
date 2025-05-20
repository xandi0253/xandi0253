"""SOMA DE NÚMEROS POSITIVOS: FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIOS NÚMEROS POSITIVOS E OS SOME.
O PROGRAMA DEVE PARAR QUANDO O USUÁRIO INSERIR UM NÚMERO NEGATIVO, UTILIZANDO WHILE"""
"""num: int = 0
num1: int = int(input("Digite um número positivo:",))
num2: int = int(input("Digite um segundo número postivo:",))

while num1 > num2 : 0
num = num1 + num2
print("Soma dos números positivo são:", num)
while num > 0:
    print(num)
    num -= 1
print()"""


print("somar dos números positivos: (Digite um número negativo para sair)")

num1 = 1
soma = 0

while num1 != 0:
    num1 = int(input("Digite um número positivo:"))
    if num1 < 0:
        break

    soma += num1

print("A soma dos números positivo digitados é:", soma)

print()