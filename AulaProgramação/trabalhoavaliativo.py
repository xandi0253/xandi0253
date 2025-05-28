'''TRABALHO PRÁTICO - Valor 1.5 Pontos (15% da nota)

Grupo de Até 6 pessoas.


Enunciado de Trabalho Prático – Desenvolvimento de uma To-Do List

Objetivo:

Desenvolver uma aplicação funcional de “To-Do List” (lista de tarefas), utilizando os conceitos de programação, organização de dados, e interface com o usuário.

Descrição:

O sistema deverá permitir ao usuário criar, visualizar, atualizar e excluir tarefas de uma lista pessoal. Além disso, deverá proporcionar uma interface clara e intuitiva, podendo ser uma aplicação de linha de comando.

Requisitos mínimos:
	1.	Adicionar tarefas: O usuário deve poder criar novas tarefas informando pelo menos uma descrição.
	2.	Listar tarefas: Exibir todas as tarefas cadastradas.
	3.	Atualizar tarefas: Permitir ao usuário marcar uma tarefa como concluída ou editar sua descrição.
	4.	Remover tarefas: Possibilitar a exclusão de tarefas da lista.
    5.  Organizar tarefas por ordem alfabética.







'''



lista_tarefas = []

while True:
    opcao: str = input(''' ================ Sistema De Tarefas ===============:
                       \t \n 1: Inserir Tarefas na Lista
                       \t \n 2: Exibir Tarefas Cadastradas
                       \t \n 3: Tarefas em Ordem Alfabética
                       \t \n 4: Remover Tarefas
                       \t \n 5: Atualizar Lista de Tarefas.
                       \t \n 6: Encerra a Lista de Tarefas.\n \n''')

    match opcao: 
        case "1":
            inserir_tarefas: str = input("Inserir - Informe a Tarefa: \n")
            lista_tarefas.append(inserir_tarefas)
            print("\n")
        case "2":
            print("======== EXIBIR TAREFAS CADASTRADAS ========",)
            for inserir_tarefas in lista_tarefas:
                print(inserir_tarefas)
            print("\n")
        case "3":
            print("======== LISTA EM ORDEM ALFABÉTICA ========",)
            for inserir_tarefas in lista_tarefas:
                lista_tarefas.sort()
                print(lista_tarefas)
            print("\n")
        case "4":
            print("======== EXIBIR TAREFAS CADASTRADAS ========",)
            excluir: str = input("Remover - Informe a Tarefa que Deseja Remover:",)
            if excluir in lista_tarefas:
                lista_tarefas.remove(excluir)
                print()
            else:
                print("Tarefa não Encontrada.",)
            print("\n")
        case "5":
            lista_tarefas.clear()
            print("\n")
        case "6":
            print("==================================== LISTA DE TAREFAS ENCERRADO! =================================== \n \n")
            break



            







