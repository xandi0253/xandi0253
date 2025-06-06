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
trabalhadas no mês, através de um parametro e exibe o salário bruto.
calcular o INSS a ser pago.
calcular o FGTS
Salario liguido.
Calcular o Impostso de renda.
Encontrar o salario liquido.

valor_hora_base: float = 45.90

def calcula_salario_bruto(numerohoras: float):
    salario_bruto:float = numerohoras * 45.90
    print(" O Salário Bruto é R$" , salario_bruto)
    
hora_trabalhadas: float = float(input(" Informe o numero de hora no mes: "))
calcula_salario_bruto(hora_trabalhadas)

def calcular_inss(salario_bruto: float):
    if salario_bruto <= 1518:
        valor_inss: float = salario_bruto * (0.075)
        print("O valor do Inss é: ", valor_inss)
    elif salario_bruto > 1518 and salario_bruto < 2793.88:
        valor_inss: float = salario_bruto * (0.09)
        print("O valor do Inss é:", valor_inss)
    elif salario_bruto > 2793.88 and salario_bruto < 4190.83:
        valor_inss: float = salario_bruto * (0.12)
    else:
        valor_inss: float = salario_bruto * (0.14)
        print(" o valor do INSS é:", valor_inss)'''
        
        
        
    
    
VALOR_HORA_BASE: float = 45.90
    
    
def calcula_salario_bruto(numerohoras: float):
    salario_bruto:float = numerohoras * VALOR_HORA_BASE
    print(" O Salário Bruto é R$" , salario_bruto)
    return salario_bruto
    
 
        
    def calcula_inss(salario_bruto: float):
        porcentual: float = 0.0
        if salario_bruto <= 1518:
            porcentual = 0.075
        elif salario_bruto > 1518 and salario_bruto < 2793.88:
            porcentual = 0.09
        elif salario_bruto > 2793.88 and salario_bruto < 4190.83:
            porcentual = 0.12
        else:
            porcentual = 0.14
        
        valor_inss: float = salario_bruto * porcentual
        print("O valor do INSS É:", valor_inss)
        
        
        
        quantidade_horas: float = float(input("Informe a quantidade de hora trabalhadas"))
        valor_salario:float = calcula_salario_bruto(quantidade_horas)
        calcula_inss(valor_salario)

    


