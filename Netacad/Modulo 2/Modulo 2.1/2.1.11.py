print("My name is", "Python.", end=" ") #- a syntax do keyword argument é end= seguido do que queremos fazer, neste exemplo demos um espaço o que faz com que a segunda frase venha aseguir a primeira em vez de haver quebra de linha
print("Monty Python.")

print("My name is", "Python.", end="") #- aqui apenas não deu o espaçamento entre linhas
print("Monty Python.")

print("My name is ", end="") #- aqui devido as strings que temos ele parece que juntou ambas as frases como uma so string
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-") #- a syntax da keyword argument é sep= seguido do simbolo/caracter que queremos dividir os argumentos, neste caso usei o - **por default é o espaço
print("My", "name", "is", "Monty", "Python.", sep=" ") #- aqui ele faz o espaçamento normal (com um espaço) entre os argumentos
print("My", "name", "is", "Monty", "Python.", sep="") #- aqui ele não faz qualquer espaçamento e coloca todos os argumentos "colados" ou seguidos entre si
print("My", "name", "is", "Monty", "Python.", sep="*") #- podemos utilizar outros caracteres (aqui o *) para separar os argumentos entre si
print("My", "name", "is", "Monty", "Python.", sep="* ") #- aqui utilizo um caracter e um espaçamento

print()
print("My", "name", "is", sep="_", end="*") #- podemos utilizar ambos os keyword argumentos juntos na mesma invocação, neste exemplo utilizei no primeiro print para separar os argumentos o _ enquanto no final o *
print("Monty", "Python.", sep="*", end="#\n") #- aqui separei os argumentos com o * e terminei com um # e um espaçamento, de novo usei ambos keyword arguments na mesma frase.