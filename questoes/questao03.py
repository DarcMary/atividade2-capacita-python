#Questão 03: Peça ao usuário uma temperatura em Celsius e converta-a para Fahrenheit. Use a fórmula F = C * 9/5 + 32.
#Feito por:Darc Mary

temperatura = input("Digite uma temperatura em graus Celsius: ")

fahrenheit = float(temperatura) * 9/5 + 32

print(f"{temperatura}°C equivale a {fahrenheit}°F")
