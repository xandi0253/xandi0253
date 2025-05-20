"""1.
Crie um programa que leia a nota de um aluno e classifique conforme abaixo:

9 a 10: Excelente

7 a 8.9: Bom

5 a 6.9: Regular


Abaixo de 5: Reprovado

"""
"""nota: float = float(input("Digite a nota do aluno:", ))

if nota >= 9 and nota <= 10:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Reprovado")


"""
"""2.
Peça ao usuário que digite a temperatura em graus Celsius.
Classifique a sensação térmica:

Acima de 35: Muito quente

Entre 25 e 35: Quente

Entre 15 e 24: Agradável

Abaixo de 15: Frio"""    

"""
temp = float(input("Digite a temperatura em graus Celsius:" ,))

if temp > 35:
    print("Muito quente")
elif temp >= 25:
    print("Quente")
elif temp >= 15:
    print("Agradavel")
else:
    print("Frio")
"""

"""
Crie um programa que peça ao usuário para digitar um número de 1 a 7 e diga qual o dia da semana correspondente:

1: Domingo

2: Segunda

3: Terça

4: Quarta

5: Quinta

6: Sexta

7: Sábado
Se digitar outro número, mostre: "Dia inválido"

"""
"""dia_da_semana = int(input("Digite o dia da semana:", ))
if dia_da_semana == 1:
    print("Domingo")
elif dia_da_semana == 2:
    print("Segunda")
elif dia_da_semana == 3:
    print("Terça")
elif dia_da_semana == 4:
    print("Quarta")
elif dia_da_semana == 5:
    print("Quinta")
elif dia_da_semana == 6:
    print("Sexta")
else:
    print("Dia da Semana invalido")

"""
"""Peça ao usuário que digite sua idade e classifique:

Menor de 12: Criança

De 12 a 17: Adolescente

De 18 a 59: Adulto

60 ou mais: Idoso
"""
"""idade: int = int(input("Digite sua Idade:", ))

if idade <= 12:
    print("criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
    """
    

"""
5.
Peça ao usuário que digite o valor de uma compra e diga qual será o desconto aplicado:

Acima de R$ 200: 20% de desconto

De R$ 100 a R$ 200: 10% de desconto

Abaixo de R$ 100: Sem desconto
"""
"""compra: float = float(input("Digite o valor da compra:R$ ", ))
if compra > 200:
    compra = compra - (compra * 0.20)
    print("O valor de compra com desconto foi de: R$", compra)
if compra >= 100:
    compra = compra - (compra * 0.10)
    print("O valor de compra com desconto foi de: R$", compra)
else:
    print("Sem Desconto")
"""