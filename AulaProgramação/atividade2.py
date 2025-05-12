'''ATIVIDADE 2
 Crie um programa que lê o conceito de um aluno na disciplina BCC201 (Introdução á Progrmação) e imprime seu segnificado, de acordo com a tabela baixo.
Caso seja informado um conceito inexistente, deve se exibida uma mensagem de erro.
Conceito significado
A Excelente
B Ótimo
C Bom
D Regular
E Ruim
F Nos vemos de novo no que vem
'''

a: str = "Execelente"
b: str = "ótimo"
c: str = "Bom"
d: str = "Regular"
e: str = "Ruim"
f: str = "Nos vemos de novo ano que vem"

conceito = input("Digite o conceito do aluno (a,b,c,d,e ou f):")

if conceito == "a": 
    print("sifnificado do conceito é:", a)
elif conceito == "b":
    print("significado do coneito é:", b)
elif conceito == "c":
    print("significado do conceito é:", c)
elif conceito == "d":
    print("significado do conceito é:", d)
elif conceito == "e":
    print("significado do conceito é:",e)

else:
    print("Erro: conceito inexistente:", f)
    


