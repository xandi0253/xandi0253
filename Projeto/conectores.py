"""CONECTORES LÓGICOS 
USADOS PARA UNIR DUAS PROPOSIÇÕES E A PARTIR DISSO PRODUZIR UM RESUOLTADO LÓGICO

- AND: PRODUZ UM RSULTADO VERDADEIRO 
QUANDO TODAS AS PROPOSIÇÕES (TESTE LÓGICO) FOREM VERDADEIRAS.
- OR: PRODUZ UM RESULTADO FALSO, QUANDO TODOS OS TESTES LOGICOS FOREM FALSOS.

A: 15 > 5
B: 10 < 8
    E                            OU
A  AND  B                     A  OR  B    
V   F   F                     V   F  F
"""


'''
Para aposentar é necessário 65 anos de idade ou 35 anos de contribuição. O sistema deve fazer a verificação
e dizer se o usuário tem direito ou não.'''

print("====== Aposentadoria ======")
idade: int = int(input("Informe a idade do  contribuinte: "))
tempo_contribuicao: int = int(input("Informe o tempo de contribuição: "))

if idade >= 65 or tempo_contribuicao >= 35:
     print("O contribuinte tem direito a aposentadoria.")
else:
     print("O contribuinte não tem direito a aposentadoria.")


'''
Para entrar em uma rede social é necessário informar um login e uma senha; 
Para teste foi criado um usuário padrão proz@25 e a senha é admin123.
Crie um sistema de login que peça ao usuário um login e uma senha e exiba a mensagem: Logado com sucesso. 
senão escreva: Login ou senha inválidos.'''

print("====== Login ======")
login: str = input("Informe o login: ")
senha: str = input("Informe a senha: ")
if login == "proz@25" and senha == "admin123":
    print("Logado com sucesso.", login)

else: 
     print("login ou senha inválidos.")


'''
CONDICIONAL - EXECUTA UM DETERMINADDO TRECHO DE CÓDIGO DE ACORDO COM UMA CONDIÇÃO

REPETIÇÃO - REPETE UM TRECHO DO CODIGO ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA
ENQUANTO (HORAIRO < 23:00) TEM AULA, '''


