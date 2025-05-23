'''7-  Faça um programa para converter um certo valor em dólar para reais (ver cotação do
dia).'''

dolar: float = 0
cotação: float = 5.65

dolar = float(input("Digite um valor em dolar:", ))
reais = dolar * cotação
print("O valor em dolar para reais é: R$", reais)
