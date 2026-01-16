#Expoentes
print(2 ** 3) #8
print(2 ** 3.) #8.0
print(2. ** 3) #8.0
print(2. ** 3.) #8.0

#Multiplicação
print(2 * 3) #6
print(2 * 3.) #6.0
print(2. * 3) #6.0
print(2. * 3.) #6.0

#Divisão
print(6 / 3) #2.0
print(6 / 3.) #2.0
print(6. / 3) #2.0
print(6. / 3.) #2.0
print("")

#Divisão inteira (arredonda o valor por baixo, ou seja ao valor menor)
print(6 // 3) #2
print(6 // 3.) #2.0
print(6. // 3) #2.0
print(6. // 3.) #2.0
print ("")

print(6 / 4) #1.5
print(6. / 4) #1.5
print(6 // 4) #1 (arrendondou por baixo)
print(6. // 4) #1.0 (arrendondou por baixo)
print ("")

print(-6 / 4) #-1.5
print(6. / -4) #-1.5
print(-6 // 4) #-2 (o resultado arredondou para baixo logo para o -2 visto ser mais pequeno que o -1, de novo mesma logica da divisão inteira sobre o resultado em inteiro)
print(6. // -4)#-2.0 (o resultado arredondou para baixo logo para o -2.0 visto ser mais pequeno que o -1.0, de novo mesma logica da divisão inteira sobre o resultado em float)
print("")

#Resto ou modulo
print(14 % 4) #=2 (resto) (print(14 // 4) = 3 que depois 3 * 4 = 12 (quociente x divisor anterior) que por fim 14 - 12 = 2 (resto))
print(14 // 4) #=3 (divisão inteira)

print(12 % 4.5) #3.0 - o resultado está em float devido ao divisor estar em float tambem e a regra anterior aplicar-se

#Adição
print(-4 + 4) #=0 (dois numeros inteiros logo o resultado é inteiro
print(-4. + 8) #=4.0 (tem um valor em float logo o resultado é em float)

#Subtração
print(-4 - 4) #-8 (subtração simples)
print(4. - 8) #-4.0 (de novo mesma regra, um argumento float resultado vai ser float)
print(-1.1) #-1.1 (valor negativo)