# Primeiro Teste Final da Ficha dos Loops

flag=True
def funcao_calculo():
    opctabuada=input("Queres fazer operaçoes ou tabuada (operacao / tabuada) ? \n")
    if opctabuada == "operacao":
        calculo=int(input("Escolhe um nº entre 1 a 1000\n"))
        calculo2=int(input("Escolhe um nº entre 1 a 1000\n"))

        if 1 <= calculo <= 1000 and 1 <= calculo2 <= 1000:
            opccalculo=input("Escolhe \n+ para soma\n- para subtração\n* para multiplicação\n/ para divisão\n")

            if opccalculo == "+":
                print(f"{calculo} + {calculo2} = {calculo2 + calculo2}")

            elif opccalculo == "-":
                print(f"{calculo} - {calculo2} = {calculo - calculo2}")

            elif opccalculo == "*":
                print(f"{calculo} * {calculo2} = {calculo * calculo2}")

            elif opccalculo == "/":
                print(f"{calculo} / {calculo2} = {calculo / calculo2}")

            else:
                print("Opção inválida")

    elif opctabuada == "tabuada":
         maxtabuada = int(input("Qual o nº máximo da tabuada? \n"))
         ncalculo=-1
         pararcalculo = False

         for i in range (1, maxtabuada + 1):
            for t in range (1, maxtabuada + 1):
                ncalculo += 1

                if ncalculo >= 20:
                    opccontinua = input("Mais 20 valores, (sim / nao) ?\n")
                    ncalculo=0

                    if opccontinua == "nao":
                        pararcalculo = True
                        break

                    elif opccontinua == "sim":
                        continue

                    else:
                        print("Resposta inválida")
                        ncalculo=20
                        continue

                print(f"{i} * {t} = {i*t}")
            print("")

            if pararcalculo == True:
                break
    else:
        print("Resposta inválida")
        return
    
def funcao_primo(analise):
    acc = 0
    print("Número | Primo | Divisores | Perfeito")

    for i in range(analise, 0, -1):
        divisores = 0
        perfeito = 0
        primo = False
        perfeitoB = False

        for a in range (1, i+1):
            if i % a == 0:
                divisores+=1

                if a != i:
                    perfeito += a

        if divisores == 2:
            primo = True

        if perfeito == i:
            perfeitoB = True
        print(f"{i:6} | {str(primo):5} | {divisores:9} | {perfeitoB}")
        acc+=1

        if acc >= 10:
            opcCont = input("Mais 10 valores (sim/nao) ?\n")

            if opcCont == "nao":
                break

            else:
                acc=0
                continue

def funcao_analise_num():
    analise = int(input("Escolhe um nº entre 1 a 30000\n"))

    while analise < 1 or analise > 30000:
        print("O numero escolhido não esta entre o parametro dado")
        analise = int(input("Escolhe um nº entre 1 a 30000\n"))

    funcao_primo(analise)
                
#Menu Inicial    
while flag:
    print("#" + 15 * "-" + " Menu " + 15 * "-" + "#") 
    print("1 - Analise de numeros")
    print("2 - Calculadora simples (+, -, *, /)")
    print("3 - Sair")
    print("#" + 36 * "-" + "#") 
    opc = input("Opçao escolhida: \n")

    if opc == "1":
        funcao_analise_num()

    if opc == "2":
        funcao_calculo()
        
    if opc == "3":
        break;    