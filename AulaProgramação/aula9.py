'''para ser aprovado em um curso o aluno deve possuir nota maior que 6 então seu status é aprovado, se for menor que 4 então seu status é reprovado e se tiver entre 4 e 6 ele esta de recuperação. crie um programa que receba uma nota e diz qual é o status do aluno.'''


nota: float = float(input("informe a nota do aluno(a)"))

if nota >= 6.0:
    print("o alundo (a)esta aprovado.")
elif nota <= 4.0:
    print("o aluno(a) esta reprovado.")
else:
    print("O aluno está de recuperação")


