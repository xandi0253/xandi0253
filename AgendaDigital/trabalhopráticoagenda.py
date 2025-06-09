''' ================== Trabalho Prático - Agenda de Contato ================='''

#Paulo Mariano - jun 07

'''Crie e entregue um documento PDF contendo:

Capturas de tela do código-fonte e da execução do programa.
Explicações detalhadas acompanhando cada trecho do código, descrevendo sua funcionalidade e propósito.

Desenvolvimento do Sistema – Agenda de Contatos
Desenvolva um sistema para gerenciar contatos, armazenando-os em um arquivo TXT. Os dados registrados para cada contato devem incluir:

Nome
Telefone
E-mail
Cidade

O sistema deverá possuir as seguintes funcionalidades:

Inserção de Contatos – Permitir ao usuário adicionar novos contatos ao arquivo.
Leitura de Contatos – Exibir os contatos armazenados no arquivo TXT.
Exclusão de Contatos – Remover registros específicos do arquivo.
Menu de Navegação – Apresentar opções para o usuário escolher qual ação deseja realizar.

Autenticação
O acesso ao sistema requer que o usuário insira a senha: proz@2025.

Encerramento do Programa
O sistema permanecerá em execução até que o usuário digite "X" para encerrá-lo.'''


print("\n==================  AGENDA DE CONTATO DIGITAL  ==================\n\n")
senha: int = "proz@2025"
senha: int = (input("Digite sua Senha Para Abrir sua Agenda Digital: "))
if senha == "proz@2025":
    print("\n        Bem vindo a Agenda Digital!!!\n        ")
else:
    print("\n        Senha inválida!!!     \n ")
    

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


