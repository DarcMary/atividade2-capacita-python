#Questão 02: Receba dois números do usuário e exiba a soma, subtração, multiplicação e divisão entre eles.
#Feito por: Darc Mary

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão: {num1} / {num2} = {divisao:.2f}")
