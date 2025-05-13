dia_semana: int = int(input("informe o número do dia:"))

match dia_semana:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("valor inválido")

''''CRIE UM MENU DE OPÇOES PARA O USUÁRIO NAVEGAR NO SISTEMA:
O MENU TEM AS SEGUINTES OPÇÕES: A - VER SALDO; B - DEPOSITAR; 
                                C - SACAR; D - ENCERRAR CONTA;
                                X - SAIR DO SISTEMA;
CASO O USUÁRIO ESCOLHKA UMA OPÇÃO DIFERENTE EXIBA: OPÇÃO INVÁLIDA.
CASO ELE ESCOLHA UMA DAS OPÇÕES CORRETAS, INFORME PARA ELE EM QUAL PARTE DO SISTEMA ELE ESTÁ.
EXEMPLO: A - SEU SALDO É DE  R$ 10000
'''

saldo: float = 10000
opcao: str = ""
opcao = input("Escolha uma opção: A - Ver saldo; B - Depositar; C - sacar; D - Encerrar conta; X - Sair do sistema:")
match opcao:
    case "A":
        print("seu saldo é de R$", saldo)
    case "B":
        deposito: float = float(input("Digite o valor do deposito:"))
        saldo = saldo + deposito
        print("seu saldo é de R$", saldo)
    case "C":
        saque: float = float(input("Digite o valor do saque:"))
        if saque > saldo:
            print("saldo insuficiente")
        else:
            saldo = saldo - saque
            print("seu saldo é de R$", saldo)
    case "D":
            print("Encerrando conta")
            saldo = 0
            print("seu saldo é de R$", saldo)
    case "X":
        print("saindo do sistema")
    case _:
        print("opção inválida")

        