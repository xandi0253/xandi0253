'''def menu():
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





if  os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            contatos = f.readlines()
            if contatos:
                for i, contato in enumerate(contatos, start=1) :
                    nome, telefone, e_mail, cidade = contato.strip( ) .split(";")
                    print(f"(i). Nome: {nome}, Telefone: {telefone}, E-mail: {e_mail}, Cidade: {cidade}")
            else:
                print("Contato Não Encontrado!!!")
    else:
        print("Arquivo de Contatos inexistente.")
    

    menu()

import os
SENHA = "proz@2025"
ARQUIVO = "contatos.txt"
def autenticar():
    senha = input("Digite a senha de acesso: ")
    if senha == SENHA:
        return True
    else:
        print("Senha incorreta.")
    return False
def inserir_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cidade = input("Cidade: ")
    with open(ARQUIVO, "a") as f:
        f.write(f"{nome};{telefone};{email};{cidade}\n")
    print("Contato adicionado com sucesso.")
def ler_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            contatos = f.readlines()
        if contatos:
            for i, contato in enumerate(contatos, start=1):
                nome, telefone, email, cidade = contato.strip().split(";")
                print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Cidade: {cidade}")
        else:
            print("Nenhum contato encontrado.")
    else:
        print("Arquivo de contatos inexistente.")
def excluir_contato():
    ler_contatos()
    num = int(input("Digite o número do contato que deseja excluir: "))
    with open(ARQUIVO, "r") as f:
        contatos = f.readlines()
    if 0 < num <= len(contatos):
        contatos.pop(num - 1)
        with open(ARQUIVO, "w") as f:
            f.writelines(contatos)
        print("Contato excluído com sucesso.")
    else:
        print("Número inválido.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir Contato")
        print("2. Ler Contatos")
        print("3. Excluir Contato")
        print("X. Sair")
        opcao = input("Escolha uma opção: ").upper()
        if opcao == "1":
            inserir_contato()
        elif opcao == "2":
            ler_contatos()
        elif opcao == "3":
            excluir_contato()
        elif opcao == "X":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")
    
if autenticar():
    menu()'''


def exibir():
   
    if  agenda:
        print("\n================ Dados do Contato  ==================\n")
        print("Nome: ", agenda["Nome"])
        print("Telefone: ", agenda["Telefone"])
        print("E-mail: ", agenda["E-mail"])
        print("Cidade: ", agenda["Cidade"])
        print("-"*40)

    else:
        print("Contato Não Encontrado!!!")

def procurar():
    nome: str = input("Qual o Contato que Deseja Procurar: ")
    encontrado = False
    try:
        with open("contatos.txt","r") as arquivo:
            for x in arquivo:
                if nome.lower() in x.lower():
                    agenda = x.strip().split(";")
                    print("-"*40)
                    print(f"Nome: {agenda[0]}")
                    print(f"Telefone: {agenda[1]}")
                    print(f"E-mail: {agenda[2]}")
                    print(f"Cidade: {agenda[3]}")
                    print("-"*40)
                    encontrado = True
                    break
        if not encontrado:
            print("-"*40)
            print("Contato não Encontrado.")
            print("-"*40)
    except FileNotFoundError:
        print("Arquivo de Contatos não Encontrado.")
       
