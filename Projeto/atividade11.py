'''11-  Faça um programa que leia a idade de um nadador e classifique-o numa das
seguintes categorias abaixo:
• Adulto (idade >= 18);
• Juvenil (idade >= 14);
• Infantil (idade >=9);
• Mirim (Idade < 9).'''

idade: int = 0
idade = int(input("Digite a idade do nadador:",))
if idade >= 18:
    print("Adulto")
elif idade >= 14:
    print("Juvenil")
elif idade >= 9:
    print("Infantil")
elif idade < 9:
    print("Mirim")
else:
    print("Idade inválida")