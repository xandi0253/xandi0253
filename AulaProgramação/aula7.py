'''faça um programa que leia do usuario o valor da quantidade de 
* calorias consumidas por dia.
o programa deve verificar se a quantidade de claorias se encontra
*na faixa de segurança - entre 1200 e 1900 cal.(incluindo amos) por dia
* o programa deve exibir como saida uma das duas informações:
* - ou exibe "dentro da faixa",
para qtd. de calorias entre 1200 e 1900.
- ou, caso contrario, exibe "fora da faixa
'''

# solitação dos valores (ENTRADA)
print("Dgite a qtd. de calorias consumidas por dia: ")
calorias = int(input())


# verificação da faixa (PROCESSAMENTO E SAIDA)
if(calorias >= 1200 and calorias <= 1900): # verifica a faixa de segurança
    print("\nDentro da faixa")
else: # caso contrario
    print("\nFora da faixa")