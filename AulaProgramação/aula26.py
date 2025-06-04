'''Crie um programa que converte o real para 3 moedas diferentes:
Euro, Dolar e Libra.
Cada uma dessas conversões deve estar em uma função diferente'''

'''
def convert_dolar (): OBSERVAÇÃO, FAZER CORREÇÃO

    cotacao_dolar: float = 5.65
    reais: float = 0
    reais = float(input("Digite um valor em reais:",))
    dolar = reais / cotacao_dolar
    
def convet_libra ():
    cotacao_libra: float = 7.63
    reais = float(input("Digite um valor em reais:",))
    libra = reais / cotacao_libra
    
    
def convert_eruro ():
    cotacao_euro: float = 6.41
    reais = float(input("Digite uma falor em reais:",))
    euro = reais / cotacao_euro

print(f" O valores em reais para,{dolar}  de libra é: {libra}, de euro é: {euro}")

convert_dolar()
convert_eruro()
convet_libra()'''


def convert_euro(valor_real: float):
    valor_euro: float = valor_real / 6.45
    print(f"O valor em euro é EU$:{valor_euro}")
    
def convert_dolar(valor_real: float):
    valor_dolar: float = valor_real / 5.45
    print(f" O valor em dolar é US$: {valor_dolar}")
    
valor_em_real: float = float(input("informe o valor: R$"))
convert_euro(valor_em_real)
convert_dolar(valor_em_real)


'''
1 - Uma empresa paga 45.90 por hora para uma analista de sistemas pleno.
Crie um programa que contém uma função que receba o número de horas
trabalhadas no mês, através de um parametro e exibe o salário bruto.'''


hora_paga = 45.90
