def menu():
    print("\n=== ESCOLHA UMA DAS OPÇÕES: ===")
    print("1. Digitar um Nome")
    print("2. Digitar um Número de Contato")
    print("3. Digitar um E-mail")
    print("4. Digitar sua Cidade")
    print("5. Exibir Os Dados da Agenda")
    print("6. Remover um Contato")
    print("7. Sair")


while True:
    menu()
    
    opcao = []
    escolha: int = input("Escolha uma Das opções Desejadas: ")
    if escolha == "1":
        escolha: int = input("Digita um Nome: ")
        opcao.append(escolha)
    print("\n")
    
    if escolha == "2":
        escolha: int = int(input("Digitar um Número de contato: "))
    print("\n")

    if escolha == "3":
        escolha: int = input("Digita um E-mail: ")
    print("\n")
    
    if escolha == "4":
        escolha: str = input("Digite uma Cidade: ")
    print("\n")

    if escolha == "5":
        for escolha in opcao:
            print(escolha)
    print("\n")
        
    if escolha == "6":
        escolha: str = input("Remover um Contato: ")
        opcao.remove(escolha)
    print("\n")

    if escolha == "7":
        print("\n====================             < AGENDA FECHADA >          ====================\n")
        break
    else:
        print("Não existe esta Opção!!!")







    menu()