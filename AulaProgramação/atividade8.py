'''8-  Faça um programa para converter um certo valor em reais para dólares (ver cotação do
dia).'''

reais: float = 0
cotação: float = 5.65

dolar = float(input("Digite um valor em reais:", ))
dolar = reais / cotação
print("O valor em reais para dolar é: R$", dolar)
