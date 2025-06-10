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

agenda = {}

def adicionar():
    nome: str = input("Qual o Nome do Contato: ")
    telefone: int = input("Qual o Telefone do Contato: ")
    e_mail: int = input("Qual o E-mail do Contato: ")
    cidade: str = input("Qual a Cidade do Contato: ")
    agenda["nome"] = nome 
    agenda["e_mail"] = e_mail
    agenda["cidade"] = cidade
    agenda["telefone"] = telefone
    print("Contato Adicionado Com Sucesso! ")

def exibir():
    print(agenda)
    if  agenda:
        print("Lista de Contatos: ")
   
    print("Nome:", agenda["nome"])

  

def procurar():
    nome: str = input("Qual o Contato que Deseja:")
    if nome in agenda:
        print("-"*40)
        print(f"Nome: {nome}")
        print(f"Telefone: {agenda[nome]}")
        print(f"E-mail: {agenda[nome]}")
        print(f"Cidade: {agenda[nome]}")
    else:
        print("Contato Não Encontrado")
    print("-"*40)

def deletar():
    nome = input("Qual o Contato que Deseja Deletar: ")
    if nome in agenda:
        del agenda[nome]
        print("-"*40)
        print("Contato Deletado Com Sucesso! ")
        print("-"*40)

def menu():
    print("\n=== ESCOLHA UMA DAS OPÇÕES: ===")
    print("1. Adiciona Seus Dados do Contato:")
    print("2. Exibir Os Dados da Agenda Digital")
    print("3. Procurar Por Contato")
    print("4. Deletar um Contato")
    print("5. Sair")

def sair_da_agenda():
    print("1. Sim")
    print("2. Não")

def repet():
    while True:
        menu()
        a = input("Escolha uma Das opções Desejadas: ")
        
        if a == "1":
            adicionar()
            sair_da_agenda()
            print("\n")
            b = input("Tem Algo Mais que Posso Ajudar:")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break
                
        
        if a == "2":
            exibir()
            sair_da_agenda()
            print("\n")
            b = input("Tem Algo Mais que Posso Ajudar:")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break
        

             
        if a == "3":
            procurar()
            sair_da_agenda()
            print("\n")
            b = input("Tem Algo Mais que Posso Ajudar:")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break
        

        if a == "4":
            deletar()
            sair_da_agenda()
            print("\n")
            b = input("Tem Algo Mais que Posso Ajudar:")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break


        if a == "5":
            print("\n====================             < AGENDA FECHADA >          ====================\n")
            break
        else:
            print("Não existe esta Opção!!!")
        

           

        

repet()





