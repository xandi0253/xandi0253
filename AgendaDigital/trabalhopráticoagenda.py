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

import os
senha = "proz@2025"
arquivo = "contatos.tx"

print("\n==================  AGENDA DE CONTATO DIGITAL  ==================\n\n")

def palavra_chave():
    senhas: int = (input("Digite sua Senha Para Abrir sua Agenda Digital: "))
    if senhas == senha:
        print("\n        Bem vindo a Agenda Digital!!!\n        ")
        return True
    else:
        print("\n        Senha inválida!!!     \n ")
        return False



def adicionar():
    print("         \n === DADOS DO CONTATO ===\n       ")
    nome: str = input("Qual o Nome do Contato: ")
    telefone: int = int(input("Qual o Telefone do Contato: "))
    e_mail: int = input("Qual o E-mail do Contato: ")
    cidade: str = input("Qual a Cidade do Contato: ")
    print("-"*30)
   
    with open(arquivo, "a") as f:
        f.write(f"{nome};{telefone};{e_mail};{cidade}\n")
    print("\n=== Contato Adicionado Com Sucesso! ===\n ")
    

def procurar_contatos():
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            contatos = f.readlines()
            if contatos:
                    print("\n                   === LISTA DE CONTATOS ===                ")
                    for lista, contato_a in enumerate(contatos, start=1):
                        nome, telefone, e_mail, cidade = contato_a.strip().split(";")
                        print(f"\n{lista}. Nome: {nome}, Telefone: {telefone}, E-mail: {e_mail}, Cidade: {cidade}\n")
                        print("-"*70)
            else:
                print("Contato não Encontrado!")
    else:
        print("Arquivo de Contato Inexistente.")
        
def deletar():
   
    procurar_contatos()
    print("\n               === DELETAR UM CONTATO ===           ")
    numero: int= int (input("\nDigite o Número que Deseja Deletar: "))
    with open(arquivo, "r") as f:
        contatos = f.readlines()
    if 0 < numero <= len(contatos) :
        contatos.pop(numero - 1)
        with open(arquivo, "w") as f:
            f.writelines(contatos)
        print("-"*30)
        print("Contato Deletado com Sucesso!")
        print("-"*30)
    else:
        print("-"*30)
        print("Número Inválido.")
        print("-"*30)

def menu():
    print("\n=== ESCOLHA UMA DAS OPÇÕES: ===\n")
    print("1. Adiciona Seus Dados do Contato")
    print("2. Procurar Contatos ")
    print("3. Deletar um Contato ")
    print("5. Sair ")

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
            b = input("Tem Algo Mais que Posso Ajudar: ")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break
        

             
        elif a == "2":
            procurar_contatos()
            sair_da_agenda()
            print("\n")
            b = input("Tem Algo Mais que Posso Ajudar: ")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break
        

        elif a == "3":
            deletar()
            sair_da_agenda()
            print("\n")
            b = input("Tem Algo Mais que Posso Ajudar: ")
            if b == "1":
                repet()
                print("\n")
            elif b == "2":
                print("Até Logo Mais")
            break


        elif a == "4":
            print("\n====================             < AGENDA FECHADA >          ====================\n")
            break
        else:
            print("Não existe esta Opção!!!")
        

           

        
if palavra_chave():
    repet()





