'''6-   Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas'''

nota1: float = 0
nota2: float = 0
nota3: float = 0

nota1 = float(input("Digite a nota1:",))
nota2 = float(input("Digite a nota2:",))
nota3 = float(input("Digite a nota3:",))

media = (nota1 + nota2 + nota3) / 3
print("Média aritmética:", media)
