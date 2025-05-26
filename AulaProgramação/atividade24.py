"""TABUADA DE UM NÚMERO: DESENVOLVA UM PROGRAMA QUE RECEBA UM NÚMERO E EXIBE SUA TABUDA DE 1 A 10 USANDO, WHILE."""
num1 = int(input("Digite um número:",))
multiplicador = 1

while multiplicador <= 10:
    resultado = num1 + multiplicador
    print(f"{num1} + {multiplicador} = {resultado}")
    multiplicador += 1
    
    

