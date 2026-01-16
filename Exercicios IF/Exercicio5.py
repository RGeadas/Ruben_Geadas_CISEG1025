# Exercício 5: Ler 3 Valores e Exibir em Ordem Crescente e Decrescente (versão manual)

num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))
num3 = int(input("Introduza o terceiro número: "))

if num1 > num2:
    num1, num2 = num2, num1  
if num2 > num3:
    num2, num3 = num3, num2  
if num1 > num2:
    num1, num2 = num2, num1  

print(f"Crescente: {num1}, {num2}, {num3}")
print(f"Decrescente: {num3}, {num2}, {num1}")
