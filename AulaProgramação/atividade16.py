# Uma tabela de uma loja é a seguinte:
'''
CÓD - PRODUTO - Valor

100 -  Camisa - 120
101 -  Saia   - 220
102 -  Calça  - 180
103 - Vestido - 350
104 -   Meia    7.50 

'''
# Crie um programa que de acordo com o código, exiba o produto e o valor:

'''
* Desafio 1:
  (Crie uma segunda versão em que o usuário além do código informe também 
   a quantidade e o programa calcula de acordo com o código informado e 
   exibe a seguinte mensagem por exemplo: A compra de 2 Camisa foi R$ 240.00)
   
* Desafio 2: Aplque um desconto de 10% se a compra for maior que R$ 500.00

'''
camisa: float = 120
saia: float = 220
calca: float = 180
vestido: float = 350
meia: float = 7.50
cod: str = ""

cod: str = str(input("Digite o código do Produto: 100 - Camisa , 101 - Saia, 220 - Calça, 103 - Vestido, 104 - Meia:", ))

match cod:
    case "100":
        print("camisa é R$", camisa )
    
    case "101":
        print("Saia é R$", saia)
    
    case "102":
        print("Calça é R$", calca)
    
    case "103":
        print("Vestido é R$", vestido)
    
    case "104":
        print("Meia é R$", meia)
    

