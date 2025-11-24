print ("Calcular a media de 10 alunos")

soma = 0

for i in range(10):
    nota = float(input("Digite a nota do " + str(i + 1) +"º aluno: "))
    soma = soma + nota

media = soma / 10

print("A média das notas é:", media)