#Questão 04: Receba uma frase do usuário e exiba a frase em letras maiúsculas, minúsculas e o número de caracteres da frase.
#Feito por:Darc Mary

frase = input("Digite uma frase: ")

frase_maiuscula = frase.upper()
frase_minuscula = frase.lower()
numero_de_caracteres = len(frase)

print(f"Frase em maiúsculas: {frase_maiuscula}")
print(f"Frase em minúsculas: {frase_minuscula}")
print(f"Número de caracteres da frase: {numero_de_caracteres}")
