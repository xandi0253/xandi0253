'''Um sacolão da desconto de 5 reais para comprar acima de 20 reais em maças. Cada maça custa 1.50, Crie um programa que receba um número de maças compradas e calcule  valor a pagar.'''

desconto: float = 5
valor: float = 20
custo: float = 1.50

quantidade = int(input("Quantos maças que comprou:"))
valor_pagar = quantidade * custo

if valor_pagar > 20:
    print("valor a  pagar: ", valor_pagar )