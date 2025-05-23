numero_1: float = 0
numero_2: float = 0
total: float = 0

numero_1 = float(input("Informe o Número: "))
numero_2 = float(input("Informe o outro Número: "))
operador_matematico: str = input("Informe a operação desejada: +, -, *, / :")

if operador_matematico == "+":
    total = numero_1 + numero_2
elif operador_matematico == "-":
    total = numero_1 - numero_2
elif operador_matematico == "*":
    total = numero_1 * numero_2
elif operador_matematico == "/":
    total = numero_1 / numero_2
else:
    print("Opção invalida")
print(" O resultado do calculo é: ", total)