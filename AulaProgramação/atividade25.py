"""FATORIAL DE UM NÚMERO: ESCREVA UM PROGRAMA QUE RECEBA UM NÚMERO E CALCULE SEU FATORIAL UTILIZANDO WHILE."""

num1 = int(input("Digite um número para calcular o fatorial:",))
fatorial = 1
contador = num1
while contador > 0:
    fatorial *= contador
    contador -= 1
    print(f"fatorial de {num1}e: {fatorial}")