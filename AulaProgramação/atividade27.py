"""CRIE UM PROGRAMA QUE CONTENHA UMA LISTA (ARRAY) COM 10 NOME EM ORDEM ALFABÉTICA.
 CRIE UM PROGRAMA QUE EXIBA ESSES NOMES EM ORDEM INVERSA."""

nomes = ["Alan", "Barbara", "Cintia", "Durval", "Eduardo", "Flávia", "Geraldo", "hércules", "Iago", "Jorge"]


for lista_nome in nomes:
    print(lista_nome)
nomes.sort(reverse=True)
print(nomes)