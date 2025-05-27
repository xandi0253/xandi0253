cidades: list = ["Betim", "Contagem", "RN", "Ibirité", "Juatuba"]
print(cidades)

#Pecorrendo uma lista(array)

#len exibe o tamanho(quantidade de elementos do array)
tamanho_lista: int = len(cidades)
"""print("O tamanho do array é", tamanho_lista)
for i range(tamanho_lista):"""
    
#Acessar um elemento pelo indice
print(cidades[4])

#forma tradicional percorrer a array(lista) pelo indice
for i in range(len(cidades)):
    print("Tradicional", cidades[i])

#Forma Avançada de percorrer o array(lista)
for item in cidades:
    print(item)



"""
for cidade in cidades:
    print("Você estar em:", cidade)"""