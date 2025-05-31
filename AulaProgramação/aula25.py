# Função é um bloco de código que pode ser chamado - sem paramentros e sem retorno


''''num1: int = int(input("Informe um número: "))
num2: int = int(input("Informe um número: "))

total: int = num1 + num2
print(" A soma total é: ", total)'''



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


'''


Crie uma  aplicativo para calcular a área de figuras geométricas:
    Quadrado:
    Triangulo:
    Retangulo:
    Circulo:
Cada cálculo deve ser feito dentro de uma função específica.
Desafio:
    Crie um sistema baseado em escolhas que de acordo com a opção
    selecionado pelo usuário a função determinada é chamada.  



'''


print("================ Calcular a área da figura geométricas ==================")

#QUADRADO:

lado: float = float(input("Informe o lado:",))
area = lado * 2
print(f"A área do Quadrado é: {area} cm",)

#Triangulo:

lado: float = float(input("Informe o lado:"))
lado: float = float(input("Informe o lado:"))
lado: float = float(input("Informe o lado:"))
area = lado + lado + lado
print(f"A área do Triangulo é: {area} cm")


#Retangulo

base: float = float(input("Informe à base:",))
altura: float = float(input("Informe à altura:",))
area = base * altura
print(f"A área do Rentângulo é: {area} cm",)

#Círculo

raio: float = float(input("Informe o raio:",))
area = pi * (raio ** 2)
print(f"A área do circulo é: {area} cm")
    






