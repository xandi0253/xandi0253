'''Um sacolão da desconto de 5 reais para comprar acima de 20 reais em maças. Cada maça custa 1.50, Crie um programa que receba um número de maças compradas e calcule  valor a pagar.'''

desconto: float = 5.00
valor: float = 20
custo: float = 1.50

quantidade = int(input("Quantos maças que comprou:"))
valor_compra = quantidade * custo

if valor_compra > 20:
    valor_compra = valor_compra - desconto
    print("valor a  pagar: ", valor_compra )