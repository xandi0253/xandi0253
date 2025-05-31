#Dicionario são estruturas do tipo coleção que armazenam dados em pares de chave e valor.



dict_carro: dict = {
     "marca": "Fiat",
     "modelo": "Uno",
     "ano": 2023,
     "cor": "Prata",
     
}

print("O modelo do carro é:", dict_carro["modelo"]) #buscando pelo chave
print("O modelo do carro é:", dict_carro.get("ano"))#buscando pelo chave

dict_proprietario: dict = {}
nome: str = input("informe o nome:")
cpf: str = input("informe o cpf:")
tel: str = input("informe o telefone:")
dict_proprietario ["nome_prop"] = nome
dict_proprietario["cpf_prop"] = cpf
dict_proprietario["tel_prop"] = tel

print(dict_proprietario)

# #Retorna as chavaes do dicionário
print(dict_carro.keys())

## print(dict_carro.values())

for item in dict_carro.keys() :
     print(dict_carro.get(item))

print(dict_carro)     
# Apagar um elemento
dict_carro.pop("marca")

del dict_carro["modelo"]
print(dict_carro)



