n = int(input("Digite um número: "))

operacoes = 0  

for i in range(1, n):
    print("Soma:", n, "+", i, "=", n + i)
    operacoes += 1

    print("Subtração:", n, "-", i, "=", n - i)
    operacoes += 1

    print("Multiplicação:", n, "*", i, "=", n * i)
    operacoes += 1

    print("Divisão:", n, "/", i, "=", n / i)
    operacoes += 1

print("\nTotal de operações efetuadas:", operacoes)