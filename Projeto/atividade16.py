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
quantidade: int = 0



cod: str = str(input("Digite o código do Produto: 100 - Camisa , 101 - Saia, 101- Calça, 103 - Vestido, 104 - Meia:", ))


match cod:
    case "100":
        quantidade: int = int(input("informe a quantidade do produto:"))
        preco = camisa * quantidade
        print(f"O Valor de {quantidade} camisa(s) é R${preco}")
    
    case "101":
        quantidade: int = int(input("informe a quantidade do produto:"))
        preco = saia * quantidade
        print(f"O Valor de {quantidade} camisa(s) é R${preco}")
       
    
    case "102":
        quantidade: int = int(input("informe a quantidade do produto:"))
        preco = calca * quantidade
        print(f"O Valor de {quantidade} camisa(s) é R${preco}")
    
    case "103":
        quantidade: int = int(input("informe a quantidade do produto:"))
        preco = vestido * quantidade
        print(f"O Valor de {quantidade} camisa(s) é R${preco}")
    
    case "104":
        quantidade: int = int(input("informe a quantidade do produto:"))
        preco = meia * quantidade
        print(f"O Valor de {quantidade} camisa(s) é R${preco}") # (OUTRO JEITO DE FAZER) print("A quantidade de meia é:",quantidade,"!","O Valor do produto é: R$", preco)

    case _:
        print("Produto não encontrado")

if preco >= 500:
   desconto: float = (preco * 0.10)
   preco = preco - desconto
   print("Seu valor com Desconto é: R$", preco)



    

