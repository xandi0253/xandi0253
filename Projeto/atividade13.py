'''13-  Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o valor da
compra for menor que 20,00; caso contrário, o lucro será de 30%. Ler o valor do produto e
imprimir o valor da venda (conforme as taxas do enunciado).'''

preco_compra: float = 0
preco_venda: float = 0
preco_compra = float(input("Digite o preço de compra do produto:",))
if preco_compra < 20:
    preco_venda = preco_compra + (preco_compra * 0.45)
    print("O preço de venda do produto é:", preco_venda)
elif preco_compra >= 20:
    preco_venda = preco_compra + (preco_compra * 0.30)
    print("O preço de venda do produto é:", preco_venda)
else:
    print("O preço de venda do produto é:", preco_venda)

    