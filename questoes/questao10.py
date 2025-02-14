#Questão 10: Peça ao usuário 4 números,
# armazene-os em uma lista e exiba a soma de todos os números.
#Feito por:Darc Mary

numeros = []

for i in range(4): 
    numero = float(input(f"Digite o {i+1}° número: "))
    numeros.append(numero)
    soma = sum(numeros)

print(f"A soma dos 4 números é: {soma}")