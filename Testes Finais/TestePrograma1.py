#Teste Programação 1

lista_aluno = []
lista_turma = []

def registar_aluno():
    
    while len(lista_aluno) >= 100 and len(lista_turma) >= 100:
        print("As listas estão cheias!")
        return

    nome_aluno = input("Escreve o nome do Aluno a registar!")
    while nome_aluno.split() == "":
       nome_aluno = input("Escreve o nome do Aluno a registar!")

    turma_aluno = input("Escreve a turma do Aluno a registar!(1-ºA, 2-ºB, 3-ºC)")
    while turma_aluno != "1-ºA" and turma_aluno != "2-ºB" and turma_aluno != "3-ºC":
        turma_aluno = input("Escreve a turma do Aluno a registar!(1-ºA, 2-ºB, 3-ºC)")

    for i in range(0,len(lista_aluno)):
        if nome_aluno == lista_aluno[i] and turma_aluno == lista_turma[i]:
            print("Esse Aluno já está registado na lista!",lista_aluno[i],lista_turma[i])
            return
        
    lista_aluno.append(nome_aluno)
    lista_turma.append(turma_aluno)

def pesquisar_aluno():
    opc = input("Queres pesquisar por turma ou por nome!\n")
    if opc == "turma":
        opc = input("Qual a turma que pretendes pesquisar?")

        for i in range(0,len(lista_aluno)):
            if  opc == lista_turma[i]:
                print("Registo encontrado",lista_aluno[i],lista_turma[i],"\nPosição:",i)
    
    elif opc == "nome":
        opc = input("Qual o nome\n")
        for i in range(0,len(lista_aluno)):
            if  opc == lista_aluno[i]:
                print("Registo encontrado",lista_aluno[i],lista_turma[i],"\nPosição:",i)

def eliminar_aluno():
    try:
        opc = int(input("Qual a posição que queres eliminar?\n"))
        del lista_aluno[opc]
        del lista_turma[opc]

    except ValueError:
        print("Erro de valor")

def ordenar_aluno():
    copia = lista_aluno.copy()
    copia.sort()
    print(copia)

def listar_tudo():
    for i in range(0,len(lista_aluno)):
        print(lista_aluno[i],lista_turma[i])

while True:
    print("#" + 23 * "-" + " Menu " + 23 * "-" + "#") 
    print("1 - Registar novo aluno")
    print("2 - Pesquisar alunos por nome ou turma")
    print("1 - Eliminar aluno por posição")
    print("1 - Ordenar por aluno de A-Z")
    print("1 - Listar Alunos e turmas que cada aluno pertence")
    print("1 - Sair do programa")
    print("#" + 52 * "-" + "#")
    print("")
    opc = int(input("Opção escolhida: "))

    if opc == 1:
        registar_aluno()
    elif opc == 2:
        pesquisar_aluno()
    elif opc == 3:
        eliminar_aluno()
    elif opc == 4:
        ordenar_aluno()
    elif opc == 5:
        listar_tudo()
    elif opc == 6:
        break 