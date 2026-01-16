#2.1 - Begin
# print("I like \"Monty Python\"") - aqui usamos o backslash (\) para que consigamos representar as quotes dentro duma string que utilizou as "" inicialmente para representar a string
# \n - Nova linha (serve para mudar de linha)
# print("") ou print('') - é "igual" desde que ambas sejam abertas/fechadas com o mesmo caracter
# print("string", end=" ") - Keyword argument que vai utilizar o caracter introduzido () no final dos argumentos, não esquecer do = e das aspas "", ou seja end="" ou sep=""
#PS: com o end=" " basicamente isto "junta" dois prints na mesma linha

# print("string", sep="*") - Keyword argument que vai utilizar o caracter introduzido (*) para separar os argumentos, pode ser utilizado em simultaneo com o end=, estes keyword são utilizados no final dos argumentos
# print("string" * 2) - isto basicamente duplica a string introduzida no print, basicamente como se fosse print("stringstring")

#2.2 - Python Literals
#print (11_111_111) - podemos escrever assim (com underscores) um numero para ser mais facil a leitura do mesmo (neste exemplo, onze milhões cento e onze mil cento e onze)
#print (0o123) - ao escrever o print com o simbolo 0o isto irá me mostrar o valor de 123 (neste exemplo) em numeração octal (sendo octal tem de ser valores entre 0 e 7)
#print (0x123) #- ao escrever o print com o simbolo 0x isto irá me mostrar o valor de 123 (neste exemplo) em numeração hexadecimal (sendo hexadecimal tem de ser valores entre 0 e f)

#4 e 4.0 são diferentes (4 é inteiro e 4.0 é float, pode tambem aparecer apenas 4.), o ponto vai definir se o numero é inteiro ou um float
#se quisermos escrever 3 x 10^8 (3 vezes 10 elevado a 8), escrevemos 3e8 (e significa expoente)
#se quisermos escrever 6.67 x 10^-34 (6.67 vezes 10 elevado a -34), escrevemos 6.67e-34 
###ATENÇÃO se escrevemos algo como print(0.0000000000000000000001) o python pode nos dar o valor de 1e-22, pois considera esta forma mais facil de ser representada

#print('I like "Monty Python"') - uma maneira mais facil para representar uma quote dentro duma string (usamos os '' em vez das quotes "" para a string)
#print('I\'m Monty Python.') ou print("I'm Monty Python.") - duas formas corretas de representar uma quote dentro duma string utilizado aspas ("") ou apostrofes ('')
#print ("") ou print ('') - isto continua a ser uma string com um valor (vazio)

#2.3 - Operadores
#Expoentes
#print(2 ** 3) = 8 - se ambos os argumentos forem numeros inteiros o resultado dá um valor inteiro
#print(2 ** 3.) ou print(2. ** 3) ou print(2. ** 3.) = 8.0 - se pelo menos um dos argumentos for float o resultado dá um float tambem.

#Multiplicação
#print(2 * 3) = 6 - se ambos os argumentos forem numeros inteiros o resultado dá um valor inteiro
#print(2 * 3.) ou print(2. * 3) ou print(2. * 3.) = 6.0 - se pelo menos um dos argumentos for float o resultado dá um float tambem.

#Divisão
#print(6 / 3) ou print(6 / 3.) ou print(6. / 3) ou print(6. / 3.) = 2.0 - o resultado na divisão independentemente do argumento ser inteiro/float dá sempre resultado float

#Divisão inteira OU floor division
#print(6 // 3) = 2 - se ambos os argumentos forem inteiros dá um resultado inteiro
#print(6 // 3.) ou print(6. // 3) ou print(6. // 3.) - se pelo menos um dos argumentos for float dá um resultado em float (mas arredondado POR BAIXO)

#print(6 / 4) ou print(6. / 4) = 1.5 - não arredondou os valores e obviamente deu-me ambos os resultados em float (divisão normal)
#print(6 // 4) = 1 e print(6. // 4) = 1.0 - no primeiro print deu me o resultado em inteiro mas ARREDONDADO POR BAIXO (1.5 para 1), no segundo print deu-me o resultado em float tambem ARRENDONDADO POR BAIXO (1.0)

#print(-6 / 4) ou print(6. / -4) = -1.5 - não arredondou os valores e resultado em float (divisão normal)
#print(-6 // 4) = -2 ou print(6.//-4) = -2.0 - no primeiro print deu me o resultado em inteiro mas ARREDONDADO POR BAIXO (-1.5 para -2), no segundo print deu-me o resultado em float tambem ARRENDONDADO POR BAIXO (-2.0)
#PS: Em numeros negativos (no exemplo acima, -2 é MENOR que -1 logo como ele ARRENDONDA PARA BAIXO, ele dá o resultado de -2 ou -2.0 (dependendo se os argumentos são int ou float)

#Resto
#print(14 % 4) = 2 - usamos a % para encontrarmos o resto da divisão desejada, se um dos divisores estiver em float o resto será em float

#Adição e subtração
#print(-4. + 8) = 4.0 - aqui aplicamos o mesmo conceito, se um dos argumentos for float o resultado será float
#print(4. - 8) = -4.0 (de novo mesma regra, um argumento float resultado vai ser float)

#EXPOENTES | [ATENÇÃO!!!] O Python lê sempre da esquerda para a direita EXCEPTO nos EXPOENTES que inverte!!!!!
#print(2 ** 2 ** 3) #= 256 (ele aqui lê ao contrario 2^3 = 8, depois 2^8 = 256) [ATENÇÃO] Nos expoentes ele lê a linha da direita para a esquerda!!!! 

#Prioridade Sinais [ALTA (PRIO 1) para mais BAIXA (PRIO 4)]
#PRIO 1 - ** (expoentes) | PRIO 2 - +,- (sinais antes dos numeros para saber se é positivo/negativo) | PRIO 3 - *,/,//,% (multiplicação, divisão, divisão inteira, resto) | PRIO 4 - +,- (mais e menos)
#PS: Se quiser fazer um expoente negativo é inserir a base e o sinal entre parenteses caso contrario o Python lê primeiro o expoente e SÓ DEPOIS o SINAL NEGATIVO!!!
#PS1: Num expoente caso o numero da direita seja negativo ele lê esse numero como negativo por exemplo 4 ** -1 = 0.25 em vez de ser -4 (onde ele lia o sinal negativo apenas APÓS o expoente ter sido feito)

#2.4 - Variaveis
#PALAVRAS PROIBIDAS COMO VARIAVEIS/FUNÇÕES
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#BOA PRATICA - O nome das variaveis/funções ser letra minuscula e separada pelo _ (underscore). As variaveis tambem tem de começar sempre por uma letra! NÃO PODE CONTER ESPAÇOS!

# var = "3.8.5"
# print("Python version: " + var) - Aqui declaramos uma variavel em string (var = "3.8.5") e o resultado será Python version: 3.8.5
#PS: O sinal de + neste contexto serve para "adicionar" à string o valor dentro da variavel var

#[ATENÇÃO] SHORTCUT OPERADORES
#No Python podemos ter shortcut operators como por exemplo [ +=, -=, *=, /=, **=, %= ] isto usamos em situações onde a variavel equivale a si mesma com outra operação!!
#EXEMPLO: var = var + 1 EQUIVALE (var += 1) || var = var - (1 * bar + par) EQUIVALE (var -= (1 * bar + par) || var = var * 10 EQUIVALE (var *= 10) || var = var / 5 * 2 EQUIVALE (var /= 5 * 2) etc.
#PS: Se retrocedermos esta operação imaginar por exemplo que temos var /= 2 * b isto é igual a var = var / (2 * b) OU SEJA TEMOS SEMPRE QUE INTRODUZIR UM PARENTESES NA EXPRESSÃO DA DIREITA SE "REVERTEMOS O SHORTCUT"

#FUNCÕES
#round () function - Esta função vai arredondar o valor às casas que inserimos, por exemplo: round(kilometers, 3) iria arredondar o valor dos kilometers para 3 casas tipo 15,235 km)

#2.5 - Comments - ATALHO CONTROL + / (Numpad) para comentar ou tirar os comments

######################################################################### 2.6 - User interaction ############################################################################################
# input () - função para que o utilizador introduza um valor | se for algo como var = input () - significa que esta variavel vai ser o valor que o utilizador escreve na consola 
#anything = input("Tell me anything... ") - Tambem podemos escrever logo no input uma string em vez de utilizarmos um print anterior com o mesmo objectivo
#se o input for uma string (como a anterior) NÃO PODEMOS fazer OPERAÇÕES ARITMETICAS com essa string introduzida no input mesmo que o utilizador tenha escrito um NUMERO (POIS O NUMERO É UMA STRING E NÃO INT/FLOAT)

# >>>>> 2.6.5 - Type Conversions <<<<<
# int(string), int(input("etc.")) ou float(string), float (input("etc.")) - estas funções convertem a string para um valor inteiro ou float

# >>>>> 2.6.6 - Input and type casting <<<<<
#Não esquecer que por vezes podemos remover uma variavel se ela servir apenas para armazenar um valor que vai ser utilizado uma vez num print. Utilizamos logo a expressão no print em vez de utilizar uma variavel

# >>>>> 2.6.7 - String Operators <<<<<
#O sinal de + quando utilizado entre duas strings (string + string), ele concatena (junta) as strings! Pode ser utilizado várias vezes numa linha/print. Exemplo: print("\nYour name is " + fnam + " " + lnam + ".")
#PS: Isto apenas faz a concatenação entre duas strings e não entre tipos diferentes (tipo uma string + inteiro)
#O sinal de * quando utilizado entre uma string e um numero, ele replica a string o NUMERO DE VEZES que o numero indicar!. Exemplo: print("string" * 2) (Ele iria replicar string 2 vezes, ou seja stringstring)
#PS: Se o numero for 0 ou negativo então não produz qualquer string!

# >>>>> 2.6.8 - More type conversions <<<<<
#str(number) - Isto faz o inverso do referido anteriormente, aqui convertemos um numero para uma string

print (88 // 60)