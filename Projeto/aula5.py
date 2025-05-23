print("====== PROGRAMA ======")

'''Crie um progroma que receba um nome, uma cidade, uma idade e exiba esses dados com as frases:
Eu sou o (A)... Moro em... Tenho...'''

nome: str = input("Digite seu nome:", )
cidade: str = input("Digite sua cidade:",)
idade: int = input("Digite sua idade:", )

print("Eu sou o (A)", nome)
print("Moro em", cidade)
print("Tenho", idade)


'''COMPARAÇÕES
Operadores Lógicos

+ soma
- subtração
* Multiplicação
/ Divisão

V - Verdadeiro
F - Falso
True = 1
False = 0
> Maior
< Menor
>= Maior ou Igual
<= Menor ou igual
!= Diferente
== Igualdade '''

num1: int = 19
num2: int = 17
restultado: bool = False
restultado = num1 > num2
print(restultado)


idade: int = int(input("Digite sua Idade:"))
restultado_lógico: bool = idade >= 18
print("O teste lógico deu:", idade )


