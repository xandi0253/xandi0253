
'''
1 - Uma empresa paga 45.90 por hora para uma analista de sistemas pleno.
Crie um programa que contém uma função que receba o número de horas
trabalhadas no mês, através de um parametro e exibe o salário bruto.'''

print("\n===================== Analista de Sistema Pleno ========================\n")
def analista_sistemas (horas_trabalhadas: float): 
    salario_bruto: float = horas_trabalhadas * 45.90
    if horas_trabalhadas <= 220:
        print(f"No total foram feitas {horas_trabalhadas} horas no mês, Salário Bruto R${salario_bruto}")
    else:
        print("Horas não permitida")

horas_trabalhadas: float = float(input("Digite quantas horas trabalhadas foram feitas no mês:",))
analista_sistemas(horas_trabalhadas)

print("\n======================== FIM DO PROGRAMA ========================\n")