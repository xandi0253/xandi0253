        

    
VALOR_HORA_BASE: float = 45.90
    
    
def calcula_salario_bruto(numero_horas: float):
    salario_bruto: float = numero_horas * VALOR_HORA_BASE
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
        
def calcula_fgts(salario_bruto: float):
        fgts: float = salario_bruto * 0.08
        print("O FGTS é R$ ", fgts)

def calclula_imposto_renda(salario_bruto: float):
    aliquita: float = 0.0
    if salario_bruto > 2428.80 and salario_bruto < 2826.65:
        aliquita = 0.075
    elif salario_bruto > 2826.65 and salario_bruto < 3751.05:
        aliquita = 0.15
    elif salario_bruto > 3751.05 and salario_bruto < 4664.68:
        aliquita = 0.0225
    elif salario_bruto < 4664.68:
        aliquita = 0.275

    
    
        
    imposto_renda: float = salario_bruto * aliquita
    print("O Imposto de renda a ser  pago é R$", imposto_renda)
    return imposto_renda



        
        
        
quantidade_horas: float = float(input("Informe a quantidade de hora trabalhadas:"))
valor_salario:float = calcula_salario_bruto(quantidade_horas)
calcula_inss(valor_salario)
calcula_fgts(valor_salario)
calclula_imposto_renda(valor_salario)





    