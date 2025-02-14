#Questão 06: Receba o nome e a idade de 3 pessoas e armazene esses dados em um dicionário. Depois exiba o dicionário completo. Para resolver essa qustão pesquise sobre Dicionários em python
#Feito por:Darc Mary

pessoas = {}

for i in range(3):
    nome = input(f"Digite o {i+1}° nome:")
    idade = float(input(f"Digite a idade do {i+1}° nome:"))
    pessoas[nome] = idade

print(f"Nome: {nome}, Idade: {idade}")
