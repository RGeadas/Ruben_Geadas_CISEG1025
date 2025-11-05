#Escreve um programa que:
#•	Peça ao utilizador dois números;
#•	Calcule a soma, subtração, multiplicação e divisão desses números;
#•	Apresente o resultado de cada operação.
#Exemplo de saída:
#Digite o primeiro número: 10
#Digite o segundo número: 2
#Soma: 12
#Subtração: 8
#Multiplicação: 20
#Divisão: 5.0


soma = 0
subtracao = 0
multiplicacao = 0
divisao = 0

num1=int(input("Digite o primeiro numero: "))
num2=int(input("Digite o segundo numero: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"Soma: {soma}")
print(f"Subtracao: {subtracao}")
print(f"Multiplicacao: {multiplicacao}")
print(f"Divisao: {divisao}")

