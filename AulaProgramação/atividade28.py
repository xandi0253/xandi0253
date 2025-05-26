"""CRIE UM PROGRAMA QUE CONTENHA OS PLANETAS DO SISTEMA SOLAR.
PERMITA AO USUÁRIO BUSCAR O NOME DO PLENETA PELA SUA POSIÇÃO NO SISTEMA SOLAR.
EX:> USUÁRIO DIGITA 2 ENTÃO O PROGRAMA EXIBE "VÊNUS"."""

sistema_solar = ["Mercúrio", "Vénus", "Terra", "Marte", "Júpiter", "Saturno", "Urano" , "Netuno" ]

for sistema in sistema_solar:
    print(sistema)

sistema: int = int(input("Digita um número para achar a posição de um planeta:", ))
if 1 <= sistema <= 8:
    print("Posição do Planeta é:", sistema_solar[sistema])
else:
    print("não tem")
