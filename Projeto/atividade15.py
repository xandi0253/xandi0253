''''CRIE UM MENU DE OPÇOES PARA O USUÁRIO NAVEGAR NO SISTEMA:
O MENU TEM AS SEGUINTES OPÇÕES: A - VER SALDO; B - DEPOSITAR; 
                                C - SACAR; D - ENCERRAR CONTA;
                                X - SAIR DO SISTEMA;
CASO O USUÁRIO ESCOLHKA UMA OPÇÃO DIFERENTE EXIBA: OPÇÃO INVÁLIDA.
CASO ELE ESCOLHA UMA DAS OPÇÕES CORRETAS, INFORME PARA ELE EM QUAL PARTE DO SISTEMA ELE ESTÁ.
EXEMPLO: A - SEU SALDO É DE  R$ 10000
'''


saldo: float = 10000
opcoes_desejada: str = ""

opcoes_desejada: str = str(input("Escolha a Opções Desejadas: A - Ver Saldo, B - Depositar, C - Sair, D - Encerrar Conta, X - Sair do Sistema:", ))

match opcoes_desejada: 
    case "A":
        print("Seu saldo é de:", saldo)
    case "B":
        deposito: float = float(input("Digite o valor que deseja depositar:",))
        saldo = saldo + deposito
        print("Seu saldo é de:", saldo)
    case "C":
        sacar: float = float(input("Digite um valor para saque:",))
        sacar = saldo - sacar
        print("Seu saldo é de:", sacar)
    case "D":
        print("Encerrar Conta")
        saldo = 0   
        print("Seu saldo é de R$:", saldo)
    case "X":
        print("Sair do Sistema")
    case _:
        print("Opção inválida "
              )