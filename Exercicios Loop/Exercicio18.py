limite = int(input("Digite um número: "))

quantidade = 0 

for n in range(1, limite + 1):

    soma = 0
    
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i

    if soma == n:
        print(n, "é um número perfeito!")
        quantidade = quantidade + 1

print("\nQuantidade de números perfeitos encontrados:", quantidade)