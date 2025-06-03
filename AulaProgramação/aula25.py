# Função é um bloco de código que pode ser chamado - sem paramentros e sem retorno


''''num1: int = int(input("Informe um número: "))
num2: int = int(input("Informe um número: "))

total: int = num1 + num2
print(" A soma total é: ", total)'''


'''
def somar():
    print("somar foi chamado")
    num1: int = int(input("Informe um número: "))
    num2: int = int(input("Informe um número: "))
    total: int = num1 + num2
    print(" A soma total é: ", total)
    
def subtrair():
    print("Subtrai foi chamado")
    num1: int = int(input("Informe um número: "))
    num2: int = int(input("Informe um número: "))
    total: int = num1 - num2
    print(" A Subtração total é: ", total)
    
    
    
    
    
somar()  #Invocar a função somar
subtrair() #Invocar a função subtrair
print("------------ Vamos somar de novo!!! ------------")
somar()





Crie uma  aplicativo para calcular a área de figuras geométricas:
    Quadrado:
    Triangulo:
    Retangulo:
    Circulo:
Cada cálculo deve ser feito dentro de uma função específica.
Desafio:
    Crie um sistema baseado em escolhas que de acordo com a opção
    selecionado pelo usuário a função determinada é chamada.'''



print("\n \n================ Calcular a área da figura geométricas ==================\n \n")

def quadrado ():
    print("============ QUADRADO: =============")
    lado: float = float(input("Informe o lado:",))
    area = lado * 2
    print(f"A área do Quadrado é: {area} cm",)

def triangulo ():
    print("\n\n============= Triangulo: =============")
    b: float = float(input("Informe à base:"))
    h: float = float(input("Informe à altura:"))
    area = (b * h) / 2
    print(f"A área do Triangulo é: {area} cm")

def retangulo ():
    print("\n\n============== Retangulo: ==============")
    base: float = float(input("Informe à base:",))
    altura: float = float(input("Informe à altura:",))
    area = base * altura
    print(f"A área do Rentângulo é: {area} cm",)

def circulo ():
    print("\n\n============== Círculo: ==============")
    pi = 3.14
    raio: float = float(input("Informe o raio:",))
    area = pi * (raio ** 2)
    print(f"A área do circulo é: {area} cm\n\n")

def forma_geometricas():
    print("\n=== 1 - Quadrado ===")
    print("\n=== 2 - Triangulo ===")
    print("\n=== 3 - Retangulo ===")
    print("\n=== 4 - Círculo ===\n")




while True:
    forma_geometricas()
    escolha = input("Digite a forma geometrica desejada:")

    if escolha =="1":
        quadrado()
    elif escolha =="2":
        triangulo()
    elif escolha =="3":
        retangulo()
    elif escolha =="4":
        circulo()
        break
    else:
        print("Opção inválida! Tente novamente!")


    





quadrado()
triangulo()
retangulo()
circulo()



