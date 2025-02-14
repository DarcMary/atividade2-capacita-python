# #Questão 05: Peça ao usuário para inserir 3 números e armazene-os em uma lista. Depois exiba a lista completa.
# #Feito por:Darc Mary

numeros = []  

for i in range(3): 
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)

print("Lista completa:", numeros) 
