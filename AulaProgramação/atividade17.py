print("************** CALCULADORA DE ÁREA **************")

pi: float = 3.14
area: float = 0.0
altura: float = 0.0
lado: float = 0.0


opcao: str = input("Informe a opção: C - Circulo, R - Retângulo, Q - Quadrado:")
match opcao:
    case "C":
        raio: float = float(input("Informe o raio:",))
        area = pi * (raio ** 2)
        print(f"A área do circulo é: {area} cm")
    
    case "R":
        base: float = float(input("Informe à base:",))
        altura: float = float(input("Informe à altura:",))
        area = base * altura
        print(f"A área do Rentângulo é: {area} cm",)

    case "Q":
        lado: float = float(input("Informe o lado:",))
        area = lado * 2
        print(f"A área do Quadrado é: {area} cm",)

    case _:
        print("área não encontrada!") 

   