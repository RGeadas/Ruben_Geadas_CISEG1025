anything = input("Enter a number: ")
something = anything ** 2.0 #Isto é impossivel concretizar devido a tentarmos fazer o expoente de uma string (mesmo que o utilizador escreva um numero como 20, pois esse 20 é string e não inteiro/float )
print(anything, "to the power of 2 is", something)

#Causa erro porque o resultado do input é uma string logo não podemos fazer uma operação aritmetica (neste caso o expoente da string introduzida no input)

