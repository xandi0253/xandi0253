"""Cria um programa que receba uma palavra e uma letra.
Conte quantas vezes a letra digitada aparece na palavra"""

palavra: str = input("Digite uma palavra:",)
letra_: str = input("Digite uma letra:",)
total: int = 0

for letra in palavra:
    print("A letra atual:", letra)
    if letra == letra_:
        total = total + 1
print(f" O total de {letra_} na palavra {palavra} é {total}")