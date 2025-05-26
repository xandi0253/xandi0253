"""CRIE UM PROGRAMA QUE CONTENHA UMA LISTA DE FRUTAS COM 10 ELEMENTOS.
PERMITA AO USUÁRIO VERFICAR SE EXISTE UMA FRUTA NA LISTA OU NÃO."""


lista_frutas: str = "banana", "laranja", "maçã", "abacate", "perâ", "morango", "kiwi","ameixa","melâncica","abacaxi"

lista_frutas = ["banana", "laranja", "maçã", "abacate", "perâ", "morango", "kiwi","ameixa","melâncica","abacaxi"]

for frutas in lista_frutas:
    print(frutas)
frutas = input("digite uma fruta:",)
if frutas == lista_frutas:
    print("Fruta encontrada:",)
else:
    print("Fruta não encontrada.",frutas)
