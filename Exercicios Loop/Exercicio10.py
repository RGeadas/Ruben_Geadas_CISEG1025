numero = int(input("Digite um número inteiro: "))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores = divisores + 1

print("O número", numero, "tem", divisores, "divisores.")