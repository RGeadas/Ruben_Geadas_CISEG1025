"""8. Operação matemática
Recebe uma operação (em texto) e dois números.
Operações válidas: "soma", "subtrai", "multiplica", "divide".
Exemplo:
Entrada →
Operação: "divide"
Número 1: 20
Número 2: 4
Saída → 5
"""

operacao = input("Operação (soma, subtrai, multiplica, divide): ").lower()
n1 = float(input("Número 1 "))
n2 = float(input("Número 2 "))

match operacao:
    case "soma":
        print(n1 + n2)
    case "subtrai":
        print(n1 - n2)
    case "multiplica":
        print(n1 * n2)
    case "divide":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")
