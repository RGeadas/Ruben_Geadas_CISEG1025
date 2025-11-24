print ("Este programa serve para calcular a media de 30 numeros pares")

soma = 0
contador = 0

while contador < 30:
    numero = int(input("Digite um número par entre 1 e 50: "))

    if numero < 1 or numero > 50:
        print("Invalido: O número deve estar entre 1 e 50.")
        continue  

    if numero % 2 != 0:
        print("Invalido: O número deve ser par.")
        continue   

    soma = soma + numero
    contador = contador + 1

media = soma / 30

print("A média dos 30 números pares é:", media)